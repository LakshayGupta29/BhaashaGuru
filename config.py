"""
Configuration module for BhaashaGuru
Handles API keys, model selection, and system parameters
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ============= API CONFIGURATION =============
# Choose provider: "huggingface", "groq", or "openrouter"
PROVIDER = os.getenv("LLM_PROVIDER", "groq")

# API Keys
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

# ============= MODEL CONFIGURATION =============
# Model selection based on provider
MODEL_CONFIGS = {
    "groq": {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",  # Groq's Llama 4 Scout model
        "api_endpoint": "https://api.groq.com/openai/v1/chat/completions",
    },
    "huggingface": {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "api_endpoint": "https://api-inference.huggingface.co/models/",
    },
    "openrouter": {
        "model": "mistralai/mistral-7b-instruct:free",
        "api_endpoint": "https://openrouter.io/api/v1/chat/completions",
    },
}

# Get current model config
CURRENT_MODEL_CONFIG = MODEL_CONFIGS.get(PROVIDER, MODEL_CONFIGS["groq"])
MODEL_NAME = os.getenv("MODEL_NAME", CURRENT_MODEL_CONFIG["model"])
API_ENDPOINT = CURRENT_MODEL_CONFIG["api_endpoint"]

# ============= GENERATION PARAMETERS =============
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))
TOP_P = float(os.getenv("TOP_P", "0.9"))

# ============= RAG CONFIGURATION =============
USE_RAG = os.getenv("USE_RAG", "false").lower() == "true"
NCERT_DOCS_PATH = os.path.join(os.path.dirname(__file__), "data", "ncert_docs")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))
TOP_K_CHUNKS = int(os.getenv("TOP_K_CHUNKS", "3"))

# ============= LANGUAGE DETECTION =============
LANGUAGE_CONFIDENCE_THRESHOLD = float(os.getenv("LANGUAGE_CONFIDENCE_THRESHOLD", "0.5"))
DEFAULT_LANGUAGE = "hi"  # Fallback language (Hindi)

# ============= SUPPORTED LANGUAGES =============
SUPPORTED_LANGUAGES = {
    "hi": "हिन्दी",
    "ta": "தமிழ்",
    "te": "తెలుగు",
    "bn": "বাংলা",
    "mr": "मराठी",
    "gu": "ગુજરાતી",
    "kn": "ಕನ್ನಡ",
    "ml": "മലയാളം",
    "en": "English",
}

# ============= DEBUG =============
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

if DEBUG:
    print(f"[DEBUG] Using LLM Provider: {PROVIDER}")
    print(f"[DEBUG] Model: {MODEL_NAME}")
    print(f"[DEBUG] RAG Enabled: {USE_RAG}")
