#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "✅ Environment ready. To activate: source venv/bin/activate"

