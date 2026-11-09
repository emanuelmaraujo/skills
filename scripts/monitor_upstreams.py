#!/usr/bin/env python3
"""Read-only monitor for curated GitHub skill repositories.
Uses only stdlib. Writes a JSON report; never clones, installs or executes upstream code.
"""
import argparse
import datetime
import json
import os
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULTS = ROOT / "upstreams.json"

def api(path, token):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "web-experience-skills-monitor"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request("https://api.github.com/" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.load(response)

def scan(manifest, token, offline=False):
    rows = []
    for item in manifest["sources"]:
        repo = item["repository"]
        row = dict(item)
        row["checked_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        if offline:
            row["result"] = "OFFLINE"
        else:
            try:
                info = api("repos/" + repo, token)
                branch = info["default_branch"]
                commit = api("repos/" + repo + "/commits/" + branch, token)
                row.update(result="OK", default_branch=branch, sha=commit["sha"],
                           archived=info["archived"], html_url=info["html_url"],
                           pushed_at=info.get("pushed_at"))
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, KeyError) as exc:
                row.update(result="ERROR", error=str(exc))
        rows.append(row)
    return {"generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "policy": manifest["policy"], "sources": rows}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=pathlib.Path, default=DEFAULTS)
    parser.add_argument("--output", type=pathlib.Path, default=pathlib.Path("upstream-report.json"))
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    assert all("/" in r["repository"] for r in data["sources"])
    report = scan(data, os.environ.get("GITHUB_TOKEN", ""), args.offline)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote report for", len(report["sources"]), "repositories:", args.output)

if __name__ == "__main__":
    main()
