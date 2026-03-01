# BhaashaGuru Architecture & Developer Guide

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Web UI (app.py)                │
├─────────────────────────────────────────────────────────────┤
│  - Question Input (any language)                            │
│  - Mode Selection (Explain/Hint)                            │
│  - Response Display with Language Detection                 │
│  - Configuration Sidebar                                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  Backend Orchestration (backend.py)         │
├─────────────────────────────────────────────────────────────┤
│ 1. detect_language()     → Language Detection               │
│ 2. retrieve_context()    → RAG System                       │
│ 3. generate_explanation()→ Prompt Building + LLM Call       │
└──────────────┬───────────────────────────────────┬──────────┘
               │                                   │
       ┌───────▼────────┐              ┌──────────▼─────┐
       │  Config (config.py)         │  Prompt Templates (prompts.py)
       │                            │
       │ - API Configuration        │ - System Instructions
       │ - Model Selection          │ - User Prompt Building
       │ - Generation Parameters    │ - Language-specific Messages
       │ - Language Support         │
       └─────────────────┘          └────────────────────┘
                                            │
                                            ▼
                    ┌───────────────────────────────────────┐
                    │    Analogy Engine (analogy_engine.py) │
                    │                                       │
                    │ - Regional Analogies Database         │
                    │ - Language-aware Selection            │
                    │ - Analogy Injection                   │
                    └─────────────────────────────────────┘
                                    │
       ┌────────────────────────────┼─────────────────────────┐
       │                            │                         │
       ▼                            ▼                         ▼
┌────────────────┐      ┌──────────────────┐     ┌─────────────────┐
│  RAG System    │      │   LLM Providers  │     │  Response       │
│  (rag.py)      │      │  (backend.py)    │     │  Formatting     │
├────────────────┤      ├──────────────────┤     └─────────────────┘
│ - NCERT Docs   │      │ • Groq API       │
│ - Text Chunking│      │ • HuggingFace    │
│ - Embeddings   │      │ • OpenRouter     │
│ - FAISS Search │      └──────────────────┘
└────────────────┘
```

## Component Specifications

### 1. Config Module (`config.py`)

**Responsibility**: Centralized configuration management

**Key Functions**:
- Load environment variables from `.env`
- Define supported languages
- Configure API endpoints
- Set generation parameters
- Initialize debug mode

**Class Structure**:
```python
# No classes - module-level configuration
PROVIDER = "groq"  # LLM provider
MODEL_CONFIGS = {...}  # Provider-specific models
TEMPERATURE = 0.7  # Generation temperature
USE_RAG = False  # RAG toggle
SUPPORTED_LANGUAGES = {...}  # Language codes
```

**Extensibility**:
- Add new LLM providers to `MODEL_CONFIGS`
- Add languages to `SUPPORTED_LANGUAGES`
- Adjust parameters via `.env` variables

### 2. Analogy Engine (`analogy_engine.py`)

**Responsibility**: Cultural localization through regional analogies

**Key Functions**:
- `get_random_analogy(language_code)`: Random analogy for language
- `inject_analogy_into_prompt()`: Add analogy to prompt
- `get_language_name()`: Get native name of language

**Data Structure**:
```python
REGIONAL_ANALOGIES = {
    "hi": {  # Hindi
        "sports": [...],
        "culture": [...],
        "nature": [...]
    },
    "ta": {...},  # Tamil
    "te": {...},  # Telugu
    # etc.
}
```

**Adding New Analogies**:
```python
REGIONAL_ANALOGIES["new_lang"] = {
    "category": [
        "Analogy text in target language"
    ]
}
```

### 3. Prompts Module (`prompts.py`)

**Responsibility**: Prompt engineering and response templates

**Key Functions**:
- `build_user_prompt()`: Construct user prompt with context
- `get_system_prompt()`: Get system instruction based on mode
- `get_fallback_message()`: Language-specific error message

**Prompt Templates**:
```python
SYSTEM_PROMPT = """You are BhaashaGuru...
Rules:
1. Respond ONLY in same language
2. Step-by-step reasoning
3. Simple vocabulary
4. Include one analogy
..."""

HINT_SYSTEM_PROMPT = """You are BhaashaGuru...
Rules:
1. ONLY first step
2. Encourage thinking
..."""
```

**Customization Points**:
- Modify `SYSTEM_PROMPT` to change tutoring style
- Update `FALLBACK_MESSAGES` for different error handling
- Adjust prompt structure in `build_user_prompt()`

### 4. RAG Module (`rag.py`)

**Responsibility**: Document retrieval and semantic search

**Class**: `SimpleRAGSystem`

**Methods**:
```python
__init__(docs_path)           # Initialize with documents
_load_documents()             # Load text files
_chunk_text(text, source)     # Split into chunks
_build_index()                # Create FAISS index
retrieve(query, top_k)        # Get relevant chunks
get_context_string(query)     # Return formatted context
```

**How It Works**:
1. Load `.txt` files from `data/ncert_docs/`
2. Split text into overlapping chunks
3. Embed chunks using `sentence-transformers`
4. Store in FAISS index (CPU-based)
5. On query: embed query, search index, return top-K results

**Customization**:
```python
# In config.py
CHUNK_SIZE = 500        # Larger = more context per chunk
CHUNK_OVERLAP = 50      # Overlap between chunks
TOP_K_CHUNKS = 3        # Results to return
```

### 5. Backend Module (`backend.py`)

**Responsibility**: Core business logic and orchestration

**Key Functions**:

```python
detect_language(text) -> (lang_code, confidence)
    # Uses langdetect to identify language

call_llm(system_prompt, user_prompt) -> response_text
    # Dispatcher to appropriate LLM provider

generate_explanation(question, language_code, mode) -> dict
    # Main function - orchestrates entire flow

format_response_for_display(response_data) -> str
    # Formats for Streamlit display
```

**LLM Provider Functions**:
```python
_call_groq(...)           # Groq API
_call_huggingface(...)    # HuggingFace API
_call_openrouter(...)     # OpenRouter API
```

**Response Dictionary Structure**:
```python
{
    "success": True,
    "question": "user question",
    "detected_language": "hi",
    "language_name": "हिन्दी",
    "language_confidence": 0.95,
    "mode": "full",  # or "hint"
    "response": "Step 1: ...\nStep 2: ...",
    "analogy": "Analogy text",
    "rag_used": False,
    "error": None
}
```

**Flow Diagram**:
```
detect_language()
        ↓
retrieve_context() [if RAG enabled]
        ↓
get_random_analogy()
        ↓
build_user_prompt()
        ↓
call_llm()
        ↓
format_response_for_display()
```

### 6. Streamlit App (`app.py`)

**Responsibility**: Web UI and user interaction

**Key Functions**:
```python
init_session_state()         # Initialize session variables
display_header()             # Show title and subtitle
display_sidebar_config()     # Configuration options
display_language_info()      # Language detection display
display_response()           # Show response with formatting
display_help_section()       # How-to guide
main()                       # Main app logic
```

**Session State**:
```python
st.session_state.history = []      # Conversation history
st.session_state.last_response = {}  # Last response
```

**UI Components**:
- Title and subtitle
- Textarea for question input
- Radio buttons for mode selection (Explain/Hint)
- Submit and Clear buttons
- Response display with custom CSS
- Sidebar for configuration
- Expandable help section
- Conversation history panel

## Data Flow Examples

### Example 1: Full Explanation in Hindi

```
User Input: "पायथागोरस प्रमेय क्या है?"
    ↓
[app.py] Question captured, mode = "full"
    ↓
[backend.py detect_language()] "पायथागोरस..." → ("hi", 0.98)
    ↓
[rag.py retrieve_context()] if USE_RAG, search NCERT docs
    ↓
[analogy_engine.get_random_analogy("hi")] Pick Hindi analogy
    ↓
[prompts.build_user_prompt()] Create prompt with all context
    ↓
[backend.call_llm()] Call Groq/HuggingFace/OpenRouter
    ↓
LLM Returns: "Step 1: पायथागोरस प्रमेय कहता है कि... Step 2:..."
    ↓
[backend.format_response_for_display()] Format with styling
    ↓
[app.py] Display in Streamlit with language badge, analogy box
    ↓
User sees complete explanation with analogy highlight
```

### Example 2: Hint Mode in Tamil

```
User Input: "வெப்ப ஆற்றல் என்றால் என்ன?" Mode: Hint
    ↓
[app.py] Question captured, mode = "hint"
    ↓
[backend.py] detect_language() → ("ta", 0.97)
    ↓
[prompts.get_system_prompt("hint")] Use HINT_SYSTEM_PROMPT
    ↓
[prompts.build_user_prompt(..., mode="hint")] 
    → "[Mode: HINT MODE (first step only)]"
    ↓
[backend.call_llm()] Call with hint system prompt
    ↓
LLM Returns: "Step 1: வெப்ப ஆற்றல் என்பது... பிறகு நீ சிந்தித்துப் பார்."
    ↓
[app.py] Display with "💡 Mode: Hint (First Step Only)"
    ↓
User gets guided hint, encouraged to think further
```

## Extension Points

### Adding a New Language

1. **In `config.py`**:
```python
SUPPORTED_LANGUAGES = {
    ...
    "xx": "Language Name",  # Add new language
}
```

2. **In `analogy_engine.py`**:
```python
REGIONAL_ANALOGIES["xx"] = {
    "category": [
        "Analogy in target language"
    ]
}

LANGUAGE_NAMES["xx"] = "Native Name"
```

3. **In `prompts.py`**:
```python
FALLBACK_MESSAGES["xx"] = "Error message in target language"
```

### Adding a New LLM Provider

1. **In `config.py`**:
```python
MODEL_CONFIGS["new_provider"] = {
    "model": "model-name",
    "api_endpoint": "https://api.example.com/v1/chat/completions",
}
```

2. **In `backend.py`**:
```python
def _call_new_provider(system_prompt, user_prompt, temp, max_tokens):
    headers = {...}
    payload = {...}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["result_field"]

# Update call_llm() dispatcher
if config.PROVIDER == "new_provider":
    return _call_new_provider(...)
```

### Adding NCERT Documents

1. Save text files to `data/ncert_docs/`
2. Format: Plain text, `.txt` extension
3. Enable in `.env`: `USE_RAG=true`
4. Automatically loaded on app start

### Modifying Analogy Injection

Edit `prompts.build_user_prompt()` to change how analogies are integrated:

```python
# Current: adds as instruction
# Could be modified to:
# - Inject within step explanations
# - Use as comparison in system prompt
# - Provide multiple analogies
```

## Future: ROCm GPU Deployment

### Current Architecture (API-based)
```python
# backend.py
def call_llm(...):
    response = requests.post(api_endpoint, ...)  # Network call
    return response.json()
```

### Future Architecture (Local GPU)
```python
# backend.py (modified for ROCm)
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LocalLLMProvider:
    def __init__(self, model_name):
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model.to('rocm')  # AMD GPU
    
    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to('rocm')
        outputs = self.model.generate(**inputs, max_new_tokens=1024)
        return self.tokenizer.decode(outputs[0])

# In config.py
if PROVIDER == "local_rocm":
    llm_engine = LocalLLMProvider("mistralai/Mistral-7B-Instruct")
    response = llm_engine.generate(prompt)
```

**Benefits of ROCm Migration**:
- ✅ No API costs or rate limits
- ✅ Offline deployment capability
- ✅ Faster inference (after warmup)
- ✅ Complete data privacy
- ✅ Full control over updates

## Performance Considerations

### Latency Breakdown (API-based)
```
Language Detection:       ~50ms   (langdetect)
RAG Retrieval:          ~200ms   (FAISS search)
Analogy Selection:       ~10ms   (random)
Prompt Building:         ~20ms   (string ops)
API Call Overhead:      ~500ms   (network latency)
LLM Inference:         2000ms    (model generation)
Response Formatting:     ~50ms   (string ops)
────────────────────────────────
Total:                 ~2.8s     (typical, varies)
```

### Optimization Tips

1. **Reduce MAX_TOKENS** in config if slower
2. **Disable RAG** if not needed (saves 200ms)
3. **Use Groq** (fastest free API)
4. **Cache embeddings** for repeated questions
5. **Deploy locally** with ROCm for best performance

## Testing Strategy

### Unit Tests (Recommended Additions)
```python
# test_backend.py
def test_language_detection():
    lang, conf = detect_language("हेलो")
    assert lang == "hi"
    assert conf > 0.5

def test_analogy_injection():
    prompt = build_user_prompt(...)
    assert "analogy" in prompt.lower() or "Analogy" in prompt

def test_fallback_message():
    msg = get_fallback_message("ta")
    assert len(msg) > 0
    assert isinstance(msg, str)
```

### Integration Tests
```python
# test_e2e.py
def test_full_flow():
    result = generate_explanation(
        "सरल प्रश्न",
        mode="full"
    )
    assert result["success"]
    assert result["detected_language"] == "hi"
    assert len(result["response"]) > 100
```

## Debugging Tips

### Enable Debug Mode
```ini
# In .env
DEBUG=true
```

### Check Language Detection
```python
from backend import detect_language
lang, conf = detect_language("Your question here")
print(f"Language: {lang}, Confidence: {conf}")
```

### Test LLM Connection
```python
from backend import call_llm, config
import prompts

response = call_llm(
    prompts.get_system_prompt(),
    "Say hello in one word"
)
print(response)
```

### Inspect Session State
```python
# In app.py, add to main():
st.sidebar.write("Debug Info:")
st.sidebar.write(st.session_state)
```

## Code Standards

### Naming Conventions
- `lowercase_with_underscores` for functions and variables
- `UPPERCASE_WITH_UNDERSCORES` for constants
- `CamelCase` for classes
- `_private_function` for internal functions

### Documentation
- Docstrings for all functions (Google style)
- Comments for complex logic
- Type hints for function signatures
- README in each module

### Error Handling
- Try-catch for external APIs
- Graceful fallbacks in user language
- Debug logging for troubleshooting
- User-friendly error messages

---

**For questions on architecture or extending the system, refer to this document and inline code comments.**
