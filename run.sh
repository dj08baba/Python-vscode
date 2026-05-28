#!/usr/bin/env bash
set -e

# Activate virtual environment if it exists, otherwise warn.
if [ -f .venv/bin/activate ]; then
  # shellcheck source=/dev/null
  . .venv/bin/activate
else
  echo "Virtual environment not found. Run: python3 -m venv .venv && . .venv/bin/activate"
  exit 1
fi

python -m src.main
