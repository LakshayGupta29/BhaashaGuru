# BhaashaGuru Installation Guide

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- An API key from one of the supported LLM providers
- Internet connection

## Step-by-Step Installation

### 1. Clone or Download the Project

```bash
cd bhaashaguru
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **streamlit**: Web UI framework
- **langdetect**: Language detection
- **requests**: HTTP client for API calls
- **faiss-cpu**: Vector similarity search
- **sentence-transformers**: Text embedding
- **huggingface_hub**: HuggingFace utilities
- **python-dotenv**: Environment variable management

### 4. Get an API Key

Choose one provider (all have free tiers):

#### Option A: Groq (Recommended - Fastest Free Option)
1. Visit https://console.groq.com
2. Sign up with Google/GitHub
3. Copy your API key from dashboard
4. Cost: FREE tier available

#### Option B: HuggingFace
1. Visit https://huggingface.co/settings/tokens
2. Create new token (read access)
3. Cost: FREE tier available

#### Option C: OpenRouter
1. Visit https://openrouter.io
2. Sign up and create API key
3. Cost: FREE tier with limited requests

### 5. Configure Environment Variables

Create `.env` file in the `bhaashaguru/` directory:

```bash
cp .env.example .env
```

Edit `.env` with your API key:

**For Groq:**
```ini
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxx
```

**For HuggingFace:**
```ini
LLM_PROVIDER=huggingface
HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxxxxxxx
```

**For OpenRouter:**
```ini
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-xxxxxxxxxxxxxxxxxx
```

### 6. Verify Installation

Test the installation:

```bash
python test_prototype.py
```

You should see output for 5 test cases in different languages.

### 7. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Troubleshooting Installation

### "Module not found" errors

Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### "API key not recognized"

1. Verify `.env` file exists in correct location
2. Check API key is valid (test on provider's website)
3. Verify `LLM_PROVIDER` spelling is correct
4. Restart terminal/IDE after creating `.env`

### "langdetect not working"

The langdetect library needs data files:
```bash
python -c "import langdetect; print(langdetect.__file__)"
```

If it says "models not found", reinstall:
```bash
pip uninstall langdetect -y
pip install langdetect
```

### "FAISS installation issues"

For CPU-only (recommended):
```bash
pip install faiss-cpu
```

### Import errors on specific OS

**macOS with Apple Silicon (M1/M2):**
```bash
pip install --upgrade --force-reinstall faiss-cpu
```

**Windows with Visual Studio Build Tools:**
Ensure C++ Build Tools are installed from:
https://visualstudio.microsoft.com/downloads/

## Verifying Setup Works

### Quick Test

```python
# In Python terminal
import streamlit
import langdetect
import faiss
import sentence_transformers
print("✅ All core modules imported successfully!")
```

### Run a Single Question

```python
from backend import generate_explanation

result = generate_explanation("What is photosynthesis?")
print(result['response'])
```

## Optional Configurations

### Enable RAG (Curriculum Context)

In `.env`:
```ini
USE_RAG=true
```

NCERT documents are pre-loaded from `data/ncert_docs/`

### Adjust Temperature (Creativity)

In `.env`:
```ini
TEMPERATURE=0.7  # 0-2.0 range
# 0.0 = deterministic/focused
# 0.7 = balanced (default)
# 2.0 = very creative/random
```

### Enable Debug Mode

In `.env`:
```ini
DEBUG=true
```

This will print detailed logs for troubleshooting.

## Docker Installation (Optional)

If you have Docker installed:

```bash
# Build image
docker build -t bhaashaguru .

# Run container
docker run -p 8501:8501 \
  -e GROQ_API_KEY=your_key \
  bhaashaguru

# Access at http://localhost:8501
```

## Testing Different Languages

After installation, test with:

```bash
# Hindi
python -c "from backend import generate_explanation; print(generate_explanation('गणित क्या है?'))"

# Tamil  
python -c "from backend import generate_explanation; print(generate_explanation('அறிவியல் என்றால் என்ன?'))"

# English
python -c "from backend import generate_explanation; print(generate_explanation('What is science?'))"
```

## Getting Help

If stuck:

1. Check `.env.example` for configuration template
2. Verify API key works on provider's website
3. Try the test suite: `python test_prototype.py`
4. Enable debug mode: `DEBUG=true` in `.env`
5. Check internet connectivity
6. Try a different LLM provider

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|------------|
| Python | 3.10 | 3.11+ |
| RAM | 4GB | 8GB+ |
| Storage | 1GB | 2GB |
| Internet | Required | Required |
| GPU | Optional | AMD ROCm-capable |

## Next Steps After Installation

1. **Read README.md** for feature overview
2. **Run test_prototype.py** to verify functionality
3. **Try different languages** in the Streamlit app
4. **Configure settings** in sidebar
5. **Add NCERT documents** to enable RAG
6. **Explore prompt templates** in `prompts.py`

## Uninstallation

To completely remove:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment folder
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# Or just delete the project folder
```

---

**You're all set! Start tutoring with BhaashaGuru! 🧠**
