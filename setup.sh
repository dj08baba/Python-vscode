#!/usr/bin/env bash
set -e

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

# shellcheck source=/dev/null
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Run ./run.sh to execute the sample."
