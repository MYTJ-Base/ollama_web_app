#!/bin/bash

set -e

echo "🔧 FIXING ISSUES AND STARTING APP"
echo "=================================="
echo ""

# Check Ollama service
echo "1️⃣  Checking Ollama status..."
if systemctl is-active --quiet ollama; then
    echo "   ✓ Ollama service is running as a background service"
else
    echo "   ! Ollama service is not active. Attempting to check port 11434..."
    if lsof -ti:11434 &>/dev/null; then
        echo "   ✓ Something is already listening on port 11434 (likely Ollama)"
    else
        echo "   ! Port 11434 is free. You may need to run 'ollama serve' manually later."
    fi
fi
echo ""

# Setup virtual environment
# Note: Using ollama_web_app_env to match your current setup
VENV_DIR="ollama_web_app_env"
echo "2️⃣  Setting up Python environment ($VENV_DIR)..."
if [ ! -d "$VENV_DIR" ]; then
    echo "   Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
echo "   ✓ Virtual environment activated"
echo ""

# Upgrade Flask
echo "3️⃣  Upgrading Flask for Python 3.14 compatibility..."
python -m pip install -q --upgrade pip setuptools wheel
python -m pip install -q 'flask>=3.1,<4' 'requests>=2.31'
echo "   ✓ Flask upgraded to version $(python -c 'import flask; print(flask.__version__)')"
echo ""

echo "✨ SETUP COMPLETE!"
echo ""
echo "📋 NEXT STEPS:"
echo ""
echo "Terminal 1: Verify Ollama (usually already running)"
echo "  $ systemctl is-active ollama"
echo ""
echo "Terminal 2: Run backend"
echo "  $ cd ~/Desktop/Development/sandbox/ollama_web_app"
echo "  $ source $VENV_DIR/bin/activate"
echo "  $ python backend.py"
echo ""
echo "Terminal 3 or Browser:"
echo "  Open: http://localhost:5000"
echo ""

if [ "$1" == "--run" ]; then
    echo ""
    echo "🚀 STARTING BACKEND SERVER..."
    echo ""
    python backend.py
fi
