# Security Policy

## Supported versions

Only the current `main` branch of the template is supported. Projects already generated from the template must apply fixes themselves; the advisory will describe what to change.

## Reporting a vulnerability

**Please do not open a public issue, discussion or pull request for a security problem.**

Report it privately through GitHub: **Security → Advisories → "Report a vulnerability"** on this repository (<https://github.com/SigmaHQ/cookiecutter-pySigma-backend/security/advisories/new>).
If you cannot use GitHub, open a public issue that says only that you have a security report and asks for a private contact. Do not include any details in that issue.

Please include:

- the template commit, the `cookiecutter` answers you used, and the generated file that shows the problem;
- the impact you see (see the scope below) and, if you have one, a proposed fix.

## What we treat as a vulnerability

This is a Cookiecutter template used to start new pySigma backends. A weakness here is copied into every backend generated from it. The following are in scope:

- **Insecure generated code:** template code that, once generated, lets rule content change the structure of generated queries or output (for example missing escaping or quoting defaults), or evaluates untrusted input.
- **Insecure generated CI/CD:** generated GitHub Actions workflows or release configuration that expose secrets, run untrusted pull-request code with elevated permissions, or could let an outsider publish a package.
- **Template execution:** hooks or template content that execute unexpected code or touch files outside the output directory when the template is rendered.

**Out of scope (report publicly as bugs):**

- Style, packaging or tooling issues without a security impact.

Problems in pySigma itself go to [SigmaHQ/pySigma](https://github.com/SigmaHQ/pySigma).

## Our process

| Step                                                                          | Target                                        |
| ----------------------------------------------------------------------------- | --------------------------------------------- |
| Acknowledge the report                                                        | within 5 working days                         |
| Initial assessment and severity (CVSS 3.1)                                    | within 14 days                                |
| Fix developed in the advisory's temporary private fork                        | as soon as practical, normally within 90 days |
| Coordinated release, then GitHub Security Advisory published (CVE via GitHub) | at the fix release                            |

- We credit reporters in the advisory unless they ask not to be credited.
- When a fix affects other SigmaHQ projects, we may coordinate their releases.
- We ask reporters to keep details private until the advisory is published or 90 days have passed, whichever comes first, unless agreed otherwise.
