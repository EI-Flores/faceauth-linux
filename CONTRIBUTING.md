# Contributing

Thank you for your interest in contributing to `faceauth-linux`.

This project is currently an early prototype. Contributions should be small, focused and easy to review.

## Current development principles

- Keep changes incremental.
- Do not modify authentication systems during early development.
- Do not touch PAM, sudo or graphical login unless explicitly planned.
- Do not commit biometric data.
- Do not commit raw camera captures.
- Do not commit local model files.
- Keep password fallback mandatory for future authentication work.
- Prefer clear documentation over hidden assumptions.

## Development setup

Create a local Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
