#!/bin/bash

# ============================================================================
# OLLAMA WEB APP - Quick Start Script
# ============================================================================
# This script helps you get started quickly
# Run: bash start.sh

echo "=========================================="
echo "🚀 OLLAMA WEB APP - Setup & Start"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Note: Using ollama_web_app_env to match your current setup
VENV_DIR="ollama_web_app_env"

if [ ! -d "$VENV_DIR" ]; then
    echo "🐍 Creating Python virtual environment ($VENV_DIR)..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

source "$VENV_DIR/bin/activate"

# Install dependencies
echo "📦 Installing/Updating Python dependencies..."
python -m pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo "✓ Dependencies ready"
echo ""

export OLLAMA_HOST="${OLLAMA_HOST:-127.0.0.1:11434}"
export OLLAMA_BASE_URL="${OLLAMA_BASE_URL:-http://$OLLAMA_HOST}"

# Check if Ollama is running
echo "🔍 Checking if Ollama is running at $OLLAMA_BASE_URL..."
if curl -s "$OLLAMA_BASE_URL/api/tags" &> /dev/null; then
    echo "✓ Ollama is running!"
else
    echo "❌ Ollama is NOT reachable!"
    echo ""
    echo "On this machine, Ollama usually runs as a system service."
    echo "Try starting/restarting it with:"
    echo "  sudo systemctl restart ollama"
    echo ""
    echo "Or start it manually if the service is not installed:"
    echo "  OLLAMA_HOST=$OLLAMA_HOST ollama serve"
    echo ""
    read -p "Press Enter after you've checked Ollama..."
fi

echo ""
echo "=========================================="
echo "🎯 Starting Backend Server..."
echo "=========================================="
echo ""
echo "The app will be available at: http://localhost:5000"
echo ""
echo "To stop the server, press Ctrl+C"
echo ""

# Start the backend
python backend.py
