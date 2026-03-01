# BhaashaGuru Quick Start - Windows (PowerShell)
# Usage: .\quickstart.ps1

Write-Host ""
Write-Host "🧠 BhaashaGuru - Multilingual STEM Tutor"
Write-Host "=========================================="
Write-Host ""

# Check Python
Write-Host "✓ Checking Python version..."
python --version
Write-Host ""

# Create virtual environment
Write-Host "✓ Creating virtual environment..."
if (-not (Test-Path "venv")) {
    python -m venv venv
    Write-Host "  Virtual environment created"
}
Write-Host ""

# Activate virtual environment
Write-Host "✓ Activating virtual environment..."
& ".\venv\Scripts\Activate.ps1"
Write-Host "  Virtual environment activated"
Write-Host ""

# Install requirements
Write-Host "✓ Installing dependencies..."
pip install -r requirements.txt | Out-Null
Write-Host "  Dependencies installed"
Write-Host ""

# Check .env
Write-Host "✓ Checking configuration..."
if (-not (Test-Path ".env")) {
    Write-Host "  ⚠️  .env file not found!"
    Write-Host "  Creating .env from template..."
    Copy-Item ".env.example" ".env"
    Write-Host "  📝 Please edit .env and add your API key"
    Write-Host ""
    Write-Host "  Supported providers:"
    Write-Host "  - Groq (fastest free): https://console.groq.com"
    Write-Host "  - HuggingFace (free): https://huggingface.co/settings/tokens"
    Write-Host "  - OpenRouter (free): https://openrouter.io"
    Write-Host ""
    Read-Host "  Press Enter once you've added your API key to .env"
} else {
    Write-Host "  ✓ Configuration found"
}
Write-Host ""

# Run tests
Write-Host "✓ Running tests..."
Write-Host ""
python test_prototype.py
Write-Host ""
Write-Host "✅ Tests completed!"
Write-Host ""

# Start app
Write-Host "✓ Starting Streamlit app..."
Write-Host ""
Write-Host "The app will open in your browser at: http://localhost:8501"
Write-Host "Press Ctrl+C to stop the app"
Write-Host ""
Write-Host "=========================================="
Write-Host ""
streamlit run app.py
