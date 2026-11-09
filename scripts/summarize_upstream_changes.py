#!/usr/bin/env python3
"""Compare GitHub upstream HEADs with a stored issue snapshot.

Only repository metadata is read. Never installs/runs third-party code or calls
an AI API. An open GitHub Issue stores the baseline; updates produce comments
only when a tracked commit SHA changes. stdlib + GitHub CLI (installed on runner).
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
from pathlib import Path

TITLE = "Radar de skills — upstreams"
START = "<!-- skill-upstreams-state\n"
END = "\n-->"
OWNER_REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")

def gh(*args):
    result = subprocess.run(
        ["gh", *args], check=True, capture_output=True, text=True, timeout=35
    )
    return result.stdout.strip()

def snapshot(body):
    match = re.search(
        re.escape(START) + r"(.*?)" + re.escape(END), body, re.DOTALL
    )
    if not match:
        return None
    value = json.loads(match.group(1))
    if not isinstance(value, dict):
        raise ValueError("Baseline must be a dictionary")
    return {str(k): str(v) for k, v in value.items()}

def issue_body(shas, date):
    metadata = json.dumps(shas, sort_keys=True, ensure_ascii=False)
    return (
        "# Radar leve — acompanhamento de skills\n\n"
        "Fonte: [upstreams.json](../blob/main/upstreams.json). "
        "Monitor somente leitura, usando GitHub Actions, Python e GitHub CLI.\n\n"
        "O SHA atualizado indica que houve alteração no repositório externo, "
        "**não** que a alteração é boa ou deve ser importada. "
        "Nada é instalado, executado, mesclado ou modificado nas suas skills.\n\n"
        "Quando usar uma skill e perceber algo a melhorar, abra uma "
        "[issue de feedback](../issues/new/choose) e compare as fontes abaixo "
        "antes de propor uma mudança pequena por PR.\n\n"
        f"Última atualização da linha de base: {date} UTC.\n\n"
        f"{START}{metadata}{END}\n"
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.report.read_text(encoding="utf-8"))
    current = {}
    failures = []
    for row in data["sources"]:
        repo = row["repository"]
        if not OWNER_REPO.fullmatch(repo):
            raise ValueError("Invalid repository in manifest: " + repo)
        if row.get("result") == "OK" and re.fullmatch(r"[0-9a-fA-F]{40}", row.get("sha", "")):
            current[repo] = row["sha"]
        else:
            failures.append(repo + " (" + row.get("result", "UNKNOWN") + ")")
    if not current:
        raise RuntimeError("All upstream queries failed; refusing to replace baseline")
    date = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not args.dry_run and not OWNER_REPO.fullmatch(repo):
        raise RuntimeError("GITHUB_REPOSITORY is invalid")
    title = TITLE
    if args.dry_run:
        print(f"DRY RUN — {len(current)} readable, {len(failures)} failed")
        return

    found = json.loads(gh("issue", "list", "--repo", repo, "--state", "open",
                          "--limit", "100", "--json", "number,title,body"))
    existing = next((r for r in found if r["title"] == title), None)
    before = snapshot(existing["body"]) if existing else None

    # Preserve last-known-good SHA when upstream temporarily fails.
    new_state = dict(before or {})
    new_state.update(current)
    state_text = issue_body(new_state, date)

    if existing is None:
        gh("issue", "create", "--repo", repo, "--title", title, "--body", state_text)
        summary = f"Baseline criada para {len(current)} fontes; nenhuma skill alterada."
    else:
        changed = [(name, before.get(name), sha) for name, sha in current.items()
                   if before and before.get(name) != sha]
        if before is None:
            changed = []  # No prior baseline: initialize without misleading alerts.
        if changed:
            lines = [f"## {date} UTC — {len(changed)} alterações upstream", "",
                     "Atualizações de origem; **exigem revisão manual** antes de qualquer adoção.", ""]
            for name, old, new in changed:
                target = f"https://github.com/{name}"
                if old:
                    target += f"/compare/{old}...{new}"
                else:
                    target += f"/commit/{new}"
                lines.append(f"- [{name}]({target}): \`{(old or 'NEW')[:12]}\` → \`{new[:12]}\`")
            lines.extend(["", "Próximo passo: somente se houver necessidade real, "
                         "analisar o diff, licença e segurança; propor um PR pequeno "
                         "com base no feedback de uso."])
            gh("issue", "comment", str(existing["number"]), "--repo", repo,
               "--body", "\n".join(lines))
        # Update SHA baseline only; never overwrite skills, README or branch.
        if new_state != (before or {}):
            gh("issue", "edit", str(existing["number"]), "--repo", repo,
               "--body", state_text)
        summary = f"{len(changed)} fontes com novos SHAs; {len(current)} verificadas."
    if failures:
        summary += " Falhas de consulta (snapshot anterior preservado): " + ", ".join(failures)
    print(summary)
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as f:
            f.write("## Radar leve de skills\n\n" + summary + "\n")

if __name__ == "__main__":
    main()
