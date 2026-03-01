#!/bin/bash
# BhaashaGuru Quick Start Script
# Run this script to set up and start the prototype

set -e

echo "🧠 BhaashaGuru - Multilingual STEM Tutor"
echo "=========================================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python --version
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
if [ ! -d "venv" ]; then
    python -m venv venv
    echo "  Virtual environment created"
fi

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null
echo "  Virtual environment activated"
echo ""

# Install requirements
echo "✓ Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1
echo "  Dependencies installed"
echo ""

# Check if .env exists
echo "✓ Checking configuration..."
if [ ! -f ".env" ]; then
    echo "  ⚠️  .env file not found!"
    echo "  Creating .env from template..."
    cp .env.example .env
    echo "  📝 Please edit .env and add your API key"
    echo ""
    echo "  Supported providers:"
    echo "  - Groq (fastest free): https://console.groq.com"
    echo "  - HuggingFace (free): https://huggingface.co/settings/tokens"
    echo "  - OpenRouter (free): https://openrouter.io"
    echo ""
    read -p "  Press Enter once you've added your API key to .env..."
else
    echo "  ✓ Configuration found"
fi
echo ""

# Run tests
echo "✓ Running tests..."
echo ""
python test_prototype.py
echo ""
echo "✅ Tests completed!"
echo ""

# Start the app
echo "✓ Starting Streamlit app..."
echo ""
echo "The app will open in your browser at: http://localhost:8501"
echo "Press Ctrl+C to stop the app"
echo ""
echo "=========================================="
streamlit run app.py
