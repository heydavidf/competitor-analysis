# Security policy

## Reporting a vulnerability

Please report security problems privately through GitHub: open the repository's **Security** tab and choose **Report a vulnerability**. Do not open a public issue.

I maintain this project on my own, so I aim to acknowledge reports within 7 days and to fix confirmed problems as soon as I reasonably can. I will credit you in the fix unless you ask me not to.

## What counts

This repository contains agent instructions, an HTML dashboard template and a small example generator. Useful reports include research text that could run script in a generated dashboard, instructions that could lead an agent to evade access controls or mishandle credentials, and anything private that was published by mistake.

## Supported versions

The latest release and the latest commit on `main` are supported. `gh skill install` installs the latest release unless you ask for another version.
