#!/bin/bash
# usage: ./setup.sh 
# requires venv, uv

if [ ! -f venv/bin/activate ]; then
    echo "venv not found. creating"
    python3 -m venv venv
fi
echo "venv found, activating"
source venv/bin/activate

uv pip install -r requirements.txt

