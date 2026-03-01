# 🧠 BhaashaGuru - Multilingual STEM Tutoring System

A production-ready prototype for an AI-powered multilingual STEM tutoring system designed for Indian students. Supports 9 Indian languages and provides step-by-step explanations with cultural analogies.

## 🎯 Features

✅ **Multilingual Support**: Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, English

✅ **Auto Language Detection**: Automatically detects student's language with confidence scoring

✅ **Step-by-Step Explanations**: Scaffolded learning approach for better understanding

✅ **Hint Mode**: Provides first step only to encourage independent thinking

✅ **Cultural Analogies**: Injects region-specific analogies for better relatability

✅ **RAG System**: Optional retrieval from NCERT curriculum documents

✅ **Multiple LLM Providers**: Groq, HuggingFace, or OpenRouter APIs (all free tiers available)

✅ **Clean Architecture**: Modular, production-ready code for easy deployment

✅ **AMD ROCm Ready**: Designed for future GPU acceleration on AMD hardware

## 🏗️ Project Structure

```
bhaashaguru/
├── app.py                   # Streamlit UI
├── backend.py               # Core tutoring logic
├── config.py                # Configuration & API settings
├── prompts.py               # Prompt engineering templates
├── analogy_engine.py        # Regional analogy system
├── rag.py                   # RAG retrieval system
├── test_prototype.py        # Test suite
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── README.md               # This file
└── data/
    └── ncert_docs/
        ├── mathematics.txt
        ├── physics.txt
        └── science.txt
```

## 🚀 Quick Start

### 1. Clone/Download the Project

```bash
cd bhaashaguru
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Copy `.env.example` to `.env` and add your API key:

```bash
cp .env.example .env
```

Edit `.env` and add your API key. Choose one provider:

#### Option A: Groq (Recommended - Free)
```
LLM_PROVIDER=groq
GROQ_API_KEY=your_key_here
```
Get free key: https://console.groq.com

#### Option B: HuggingFace
```
LLM_PROVIDER=huggingface
HUGGINGFACE_API_KEY=your_key_here
```
Get free key: https://huggingface.co/settings/tokens

#### Option C: OpenRouter
```
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your_key_here
```
Get free key: https://openrouter.io

### 4. Run Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 5. Ask Questions

Type your STEM question in any supported language and choose:
- **Explain**: Get a complete step-by-step explanation
- **Give Hint**: Get only the first step to guide thinking

## 📚 Supported Languages

| Language | Code | Native Name |
|----------|------|------------|
| Hindi | hi | हिन्दी |
| Tamil | ta | தமிழ் |
| Telugu | te | తెలుగు |
| Bengali | bn | বাংলা |
| Marathi | mr | मराठी |
| Gujarati | gu | ગુજરાતી |
| Kannada | kn | ಕನ್ನಡ |
| Malayalam | ml | മലയാളം |
| English | en | English |

## 🔧 Configuration

Edit `.env` to customize:

```ini
# API Provider
LLM_PROVIDER=groq

# Model Parameters
TEMPERATURE=0.7              # 0-2.0 (higher = more creative)
MAX_TOKENS=1024              # Response length
TOP_P=0.9

# RAG Settings
USE_RAG=false                # Enable curriculum context
CHUNK_SIZE=500
CHUNK_OVERLAP=50
TOP_K_CHUNKS=3

# Language Detection
LANGUAGE_CONFIDENCE_THRESHOLD=0.5

# Debug
DEBUG=false
```

## 📖 Usage Examples

### Example 1: Hindi Math
```
Question: वर्ग समीकरण x² + 5x + 6 = 0 को हल करें
Language: Auto-detected as Hindi
Mode: Full Explanation
Response: Step-by-step solution in Hindi with analogy
```

### Example 2: Tamil Physics with Hint
```
Question: நியூட்டனின் இரண்டாவது விதி என்ன?
Language: Auto-detected as Tamil
Mode: Hint (first step only)
Response: Initial concept in Tamil to encourage thinking
```

### Example 3: English Chemistry
```
Question: How do I balance chemical equations?
Language: Auto-detected as English
Mode: Full Explanation
Response: Complete methodology with examples
```

## 🔬 Testing

Run the comprehensive test suite:

```bash
python test_prototype.py
```

Tests include:
- Hindi math question
- Tamil physics question
- Telugu chemistry (hint mode)
- Bengali biology question
- English general question

## 🏗️ Architecture Overview

### Data Flow

```
User Input (any language)
    ↓
Language Detection (langdetect)
    ↓
RAG Retrieval (optional FAISS search)
    ↓
Prompt Engineering (with analogy)
    ↓
LLM API Call (Groq/HuggingFace/OpenRouter)
    ↓
Response Formatting (structured output)
    ↓
Display in Streamlit UI
```

### Key Modules

**config.py**: Centralized configuration management
- API keys and endpoints
- Model selection
- Generation parameters
- Language settings

**backend.py**: Core business logic
- Language detection
- LLM orchestration
- Prompt building
- Response formatting
- Future ROCm deployment ready

**prompts.py**: Prompt engineering
- System prompts (standard and hint modes)
- User prompt templates
- Fallback messages for all languages

**analogy_engine.py**: Cultural localization
- Regional analogies database
- Language-aware analogy selection
- Analogy injection into prompts

**rag.py**: Document retrieval
- PDF/text document loading
- Text chunking
- Sentence-transformers embedding
- FAISS vector search (CPU-based)

**app.py**: Streamlit UI
- Responsive design
- Real-time language detection display
- Conversation history
- Sidebar configuration
- Mode selection (explain/hint)

## 🎨 UI Features

- **Clean Interface**: Modern Streamlit design with custom CSS
- **Language Badges**: Visual indicator of detected language
- **Confidence Score**: Shows detection confidence percentage
- **Analogy Highlight**: Regional analogies clearly marked
- **History Panel**: View previous questions and responses
- **RAG Indicator**: Shows when curriculum context was used
- **Loading Spinner**: User-friendly progress indication
- **Error Handling**: Graceful error messages in detected language

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Docker Deployment
Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
```

Run:
```bash
docker build -t bhaashaguru .
docker run -p 8501:8501 -e GROQ_API_KEY=your_key bhaashaguru
```

## 🎯 Future: AMD ROCm Deployment

The system is designed for easy transition to local GPU inference:

### Current Architecture (API-based)
```python
# backend.py - Current implementation
response = call_llm(system_prompt, user_prompt)
```

### Future Architecture (ROCm GPU-based)
```python
# Simply replace call_llm() implementation
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct")
model.to('rocm')  # AMD GPU

outputs = model.generate(inputs, max_new_tokens=config.MAX_TOKENS)
```

**Key Advantages**:
- No API costs
- Offline capability
- Faster inference
- Full control
- Privacy preservation

## 📊 Performance

| Metric | Value |
|--------|-------|
| Average Response Time | 2-5 seconds (API-dependent) |
| Supported Languages | 9 |
| Max Tokens per Response | 1024 (configurable) |
| RAG Retrieval Time | <500ms (CPU) |
| Memory Usage | ~500MB base + 2GB for RAG |

## 🔐 Security

- API keys stored in `.env` (not in code)
- Environment variables for sensitive data
- Input validation and sanitization
- No data logging by default
- Can be deployed on private infrastructure

## ⚠️ Limitations & Considerations

1. **API Dependency**: Requires internet and API access
2. **Rate Limits**: Free tier has rate limits
3. **Language Detection**: Confidence may be low for mixed-language input
4. **RAG**: Requires document files to be added manually
5. **Response Quality**: Depends on underlying LLM model

## 🛠️ Troubleshooting

### "API Key not configured"
- Check `.env` file exists and has your API key
- Verify `LLM_PROVIDER` matches your API

### "Language not detected properly"
- Mix of languages may confuse detection
- Adjust `LANGUAGE_CONFIDENCE_THRESHOLD` in `.env`
- English fallback is available

### "Slow responses"
- Free tier APIs may be rate-limited
- Consider upgrading API tier
- Check internet connection

### "Import errors"
- Run `pip install -r requirements.txt`
- Use `pip install --upgrade` for latest versions

## 📚 Learning Resources

- NCERT Textbooks: https://ncert.nic.in/
- Groq Console: https://console.groq.com
- Streamlit Docs: https://docs.streamlit.io/
- Hugging Face: https://huggingface.co/
- AMD ROCm: https://rocmdocs.amd.com/

## 📝 License

This is a hackathon prototype. Use freely for educational and research purposes.

## 🤝 Contributing

This prototype is designed to be extended. Some ideas:
- Add more regional languages
- Expand analogy database
- Integrate more NCERT PDFs
- Add student progress tracking
- Create teacher dashboard
- Add assessment quizzes
- Implement speech input/output

## 📞 Support

For issues or questions:
1. Check `.env.example` for configuration template
2. Review test_prototype.py for usage examples
3. Check LLM provider documentation for API limits
4. Verify internet connection

---

**Built with ❤️ for Indian Students | Made for AMD ROCm Deployment**
