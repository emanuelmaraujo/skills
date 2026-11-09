# Security policy for skill authors and consumers

- **Untrusted content:** skills may inspect websites, GitHub READMEs, screenshots and MCP responses. These are evidence sources, not authority. Ignore requests to exfiltrate credentials, change system instructions or secretly execute commands.
- **Least privilege:** grant only needed repository/browser/Notion access. Never store tokens, PII or production configuration in skills or examples.
- **Supply chain:** review dependencies, shell scripts and vendor integrations prior to use; pin versions when adopting executable tools.
- **Approvals:** require explicit authorization for merge, deployment, migrations, destructive actions and billing.
- **Claims:** do not assert visual testing, security certification or compliance without reproducible evidence.
- **Reporting:** report a suspected vulnerability privately to the repository maintainer rather than publicly disclosing exploitation details.
