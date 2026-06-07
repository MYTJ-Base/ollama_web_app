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

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo "✓ Dependencies installed"
echo ""

# Check if Ollama is running
echo "🔍 Checking if Ollama is running on port 11434..."
if curl -s http://localhost:11434/api/tags &> /dev/null; then
    echo "✓ Ollama is running!"
else
    echo "❌ Ollama is NOT running!"
    echo ""
    echo "To start Ollama, open a NEW terminal and run:"
    echo "  ollama serve"
    echo ""
    echo "After Ollama starts, pull the Qwen model:"
    echo "  ollama pull qwen"
    echo ""
    read -p "Press Enter after you've started Ollama..."
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
python3 backend.py
