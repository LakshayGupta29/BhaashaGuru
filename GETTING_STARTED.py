#!/usr/bin/env python3
"""
BhaashaGuru - Comprehensive Getting Started Guide

This file provides an overview of the entire prototype system.
Run this to understand how to use and extend BhaashaGuru.
"""

SYSTEM_OVERVIEW = """
╔════════════════════════════════════════════════════════════════════════════╗
║                        🧠 BhaashaGuru - Quick Guide                        ║
║                  Multilingual STEM Tutoring System (v1.0)                  ║
╚════════════════════════════════════════════════════════════════════════════╝

BhaashaGuru is a production-ready AI-powered tutoring system that:
  • Answers STEM questions in 9 Indian languages (auto-detected)
  • Provides step-by-step explanations with cultural analogies
  • Offers hint mode for guided learning
  • Integrates with NCERT curriculum via RAG
  • Uses free LLM APIs (Groq, HuggingFace, OpenRouter)
  • Is designed for future AMD ROCm GPU deployment

═══════════════════════════════════════════════════════════════════════════════
"""

QUICK_START = """
🚀 QUICK START (5 minutes)

1. Copy .env.example to .env:
   cp .env.example .env

2. Edit .env with your API key:
   LLM_PROVIDER=groq
   GROQ_API_KEY=your_api_key_here
   
   Get free key: https://console.groq.com

3. Run the app:
   streamlit run app.py

4. Ask a question in any language:
   • "वर्ग समीकरण कैसे हल करते हैं?" (Hindi)
   • "நியூட்டனின் விதிகள் யாவை?" (Tamil)
   • "What is photosynthesis?" (English)

═══════════════════════════════════════════════════════════════════════════════
"""

PROJECT_STRUCTURE = """
📁 PROJECT STRUCTURE

bhaashaguru/
│
├── 📄 Core Application Files:
│   ├── app.py                  # Streamlit UI (start here!)
│   ├── backend.py              # Core logic & orchestration
│   ├── config.py               # Configuration management
│   ├── prompts.py              # Prompt templates
│   ├── analogy_engine.py       # Cultural analogies
│   ├── rag.py                  # Document retrieval system
│   └── test_prototype.py       # Test suite
│
├── 📚 Documentation:
│   ├── README.md               # Feature overview & usage
│   ├── INSTALLATION.md         # Step-by-step setup
│   ├── ARCHITECTURE.md         # Technical deep-dive
│   ├── FEATURES.md             # Feature checklist
│   └── GETTING_STARTED.md      # This file
│
├── ⚙️ Configuration:
│   ├── .env.example            # Environment variables template
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Your API key (create from .env.example)
│
├── 🚀 Quick Start Scripts:
│   ├── quickstart.sh           # Linux/macOS setup script
│   ├── quickstart.bat          # Windows batch script
│   └── quickstart.ps1          # Windows PowerShell script
│
└── 📊 Data:
    └── data/ncert_docs/        # NCERT curriculum documents
        ├── mathematics.txt
        ├── physics.txt
        └── science.txt

═══════════════════════════════════════════════════════════════════════════════
"""

FILE_DESCRIPTIONS = """
📋 WHAT EACH FILE DOES

CORE APPLICATION:
─────────────────
✓ app.py
  - Streamlit web interface
  - Question input and response display
  - Language detection visualization
  - Configuration sidebar
  - Conversation history
  → START HERE to see the UI

✓ backend.py
  - Language detection (langdetect)
  - LLM API calls (Groq/HuggingFace/OpenRouter)
  - Prompt orchestration
  - Response formatting
  → Contains main generate_explanation() function

✓ config.py
  - Centralized configuration
  - API keys and endpoints
  - Model selection
  - Generation parameters (temperature, max_tokens, etc.)
  - Language definitions
  → Edit to switch LLM providers or adjust parameters

✓ prompts.py
  - System prompts (instructions for the AI)
  - User prompt templates
  - Language-specific fallback messages
  → Modify to change tutoring style or tone

✓ analogy_engine.py
  - Regional analogy database
  - Language-aware analogy selection
  - Analogy injection into prompts
  → Add analogies for new languages here

✓ rag.py
  - RAG (Retrieval-Augmented Generation) system
  - Document loading and chunking
  - FAISS vector search
  - Context retrieval for prompts
  → Currently optional, add NCERT PDFs to data/ncert_docs/ to enable

✓ test_prototype.py
  - Comprehensive test suite
  - Tests in 5 different languages
  - Hint mode testing
  - Error handling verification
  → Run to verify installation: python test_prototype.py

DOCUMENTATION:
──────────────
✓ README.md
  - Feature overview
  - Supported languages
  - Configuration guide
  - Deployment options
  → Main documentation file

✓ INSTALLATION.md
  - Step-by-step setup instructions
  - Troubleshooting guide
  - Virtual environment setup
  - Dependency installation
  → Follow if you have setup issues

✓ ARCHITECTURE.md
  - System architecture diagrams
  - Component specifications
  - Data flow examples
  - Extension points for developers
  → Read if you want to understand or modify the system

✓ FEATURES.md
  - Complete feature checklist
  - What's implemented
  - Performance metrics
  - Future enhancements
  → Reference for feature status

CONFIGURATION:
──────────────
✓ .env.example
  - Template for environment variables
  - Configuration options explained
  - API provider options
  → Copy to .env and fill in your API key

✓ requirements.txt
  - All Python dependencies
  - Version specifications
  → Run: pip install -r requirements.txt

QUICK START SCRIPTS:
────────────────────
✓ quickstart.sh (Linux/macOS)
  - Automated setup script
  - Creates virtual environment
  - Installs dependencies
  - Runs tests
  - Starts the app
  → Run: bash quickstart.sh

✓ quickstart.bat (Windows Command Prompt)
  - Windows batch version of setup
  → Run: quickstart.bat

✓ quickstart.ps1 (Windows PowerShell)
  - Windows PowerShell version
  → Run: .\quickstart.ps1

═══════════════════════════════════════════════════════════════════════════════
"""

SUPPORTED_LANGUAGES = """
🌐 SUPPORTED LANGUAGES (9 total)

Language    | Code | Native Name     | Example Question
─────────────────────────────────────────────────────────────────
Hindi       | hi   | हिन्दी          | "गुरुत्वाकर्षण क्या है?"
Tamil       | ta   | தமிழ்           | "வட்டத்தின் பரப்பளவு?"
Telugu      | te   | తెలుగు          | "కెమికల్ రియాక్షన్?"
Bengali     | bn   | বাংলা          | "আলোর গতি কত?"
Marathi     | mr   | मराठी           | "शक्ती म्हणजे काय?"
Gujarati    | gu   | ગુજરાતી          | "ભૌતિક વિજ્ઞાન શું છે?"
Kannada     | kn   | ಕನ್ನಡ            | "ಪಡೆ ಎಂದರೇನು?"
Malayalam   | ml   | മലയാളം          | "എനർജി എന്നാണ്?"
English     | en   | English         | "What is evolution?"

Auto-detection: System automatically identifies language from input
Fallback: If detection confidence is low, defaults to Hindi
Confidence: Display shows detection confidence percentage

═══════════════════════════════════════════════════════════════════════════════
"""

LLM_PROVIDERS = """
🤖 LLM PROVIDER OPTIONS (all free!)

Provider      | Cost          | Speed | Quality | Recommendation
──────────────────────────────────────────────────────────────────
Groq          | FREE          | ⚡⚡⚡  | ⭐⭐⭐ | ✅ BEST for free tier
HuggingFace   | FREE          | ⚡⚡   | ⭐⭐   | Good alternative
OpenRouter    | FREE (limited)| ⚡⚡   | ⭐⭐⭐ | Good quality

Setup (Choose ONE):

1️⃣ GROQ (Recommended):
   - Visit: https://console.groq.com
   - Sign up with Google/GitHub
   - Copy API key
   - Set in .env:
     LLM_PROVIDER=groq
     GROQ_API_KEY=your_key

2️⃣ HUGGINGFACE:
   - Visit: https://huggingface.co/settings/tokens
   - Create new token
   - Set in .env:
     LLM_PROVIDER=huggingface
     HUGGINGFACE_API_KEY=your_key

3️⃣ OPENROUTER:
   - Visit: https://openrouter.io
   - Create API key
   - Set in .env:
     LLM_PROVIDER=openrouter
     OPENROUTER_API_KEY=your_key

═══════════════════════════════════════════════════════════════════════════════
"""

FEATURE_OVERVIEW = """
✨ KEY FEATURES

1. AUTO LANGUAGE DETECTION
   ✓ Detects language from input automatically
   ✓ Shows detection confidence
   ✓ Graceful fallback if uncertain

2. STEP-BY-STEP EXPLANATIONS
   ✓ Structured learning with numbered steps
   ✓ Suitable for Class 8-12 students
   ✓ Clear, simple language

3. HINT MODE
   ✓ "Give Hint" button for first-step guidance
   ✓ Encourages independent thinking
   ✓ Helps with stuck students

4. CULTURAL ANALOGIES
   ✓ Region-specific examples (cricket, temples, farming, etc.)
   ✓ Makes concepts relatable
   ✓ Improves retention
   ✓ Different for each language

5. RAG SYSTEM (Optional)
   ✓ Retrieves relevant NCERT curriculum content
   ✓ Makes responses curriculum-aware
   ✓ Includes proper citations
   ✓ CPU-only (no GPU needed)

6. CONFIGURATION OPTIONS
   ✓ Temperature control (0.0-2.0)
   ✓ Max tokens per response
   ✓ RAG toggle
   ✓ Language confidence threshold

7. CONVERSATION HISTORY
   ✓ View previous questions
   ✓ Quickly access past responses
   ✓ Session-based storage

8. ERROR HANDLING
   ✓ API failure fallbacks
   ✓ Error messages in student's language
   ✓ Debug mode for troubleshooting

═══════════════════════════════════════════════════════════════════════════════
"""

USAGE_EXAMPLES = """
📖 USAGE EXAMPLES

EXAMPLE 1: Hindi Math Question
──────────────────────────────
Question: "वर्ग समीकरण x² + 5x + 6 = 0 को हल करें"
Mode: Explain (full)
Output:
  🌐 Detected Language: हिन्दी (98% confidence)
  📚 Mode: Full Explanation
  
  Step 1: समीकरण को ax² + bx + c = 0 के रूप में पहचानें
  Step 2: गुणनखंड विधि का उपयोग करें...
  Step 3: समाधान प्राप्त करें x = -2 या x = -3
  
  🎯 Regional Analogy: "जैसे खेती में बीज बोने से पहले..."

EXAMPLE 2: Tamil Physics - Hint Mode
────────────────────────────────────
Question: "நியூட்டனின் இரண்டாவது விதி என்ன?"
Mode: Give Hint (first step)
Output:
  🌐 Detected Language: தமிழ் (95% confidence)
  💡 Mode: Hint (First Step Only)
  
  Step 1: நியூட்டனின் இரண்டாவது விதி என்பது...
  
  🎯 Regional Analogy: "கோவில் கட்டடம் போல் விஞ்ஞானமும்..."

EXAMPLE 3: English Question
───────────────────────────
Question: "What is photosynthesis?"
Mode: Explain (full)
Output:
  🌐 Detected Language: English (99% confidence)
  📚 Mode: Full Explanation
  
  Step 1: Photosynthesis is the process where...
  Step 2: Two main stages occur...
  Step 3: The equation is...
  
  🎯 Regional Analogy: "Like a factory converting raw materials..."
  
  📖 This response was enhanced with NCERT curriculum context.

═══════════════════════════════════════════════════════════════════════════════
"""

CONFIGURATION_GUIDE = """
⚙️ CONFIGURATION GUIDE

Edit .env file to customize:

API CONFIGURATION:
──────────────────
LLM_PROVIDER=groq                    # Choose: groq, huggingface, openrouter
GROQ_API_KEY=your_key                # Your API key (choose your provider)
HUGGINGFACE_API_KEY=your_key         # Or this one
OPENROUTER_API_KEY=your_key          # Or this one

MODEL CONFIGURATION:
────────────────────
MODEL_NAME=mixtral-8x7b-32768        # LLM model to use
TEMPERATURE=0.7                      # 0=focused, 1=balanced, 2=creative
MAX_TOKENS=1024                      # Max response length
TOP_P=0.9                            # Nucleus sampling

RAG CONFIGURATION:
───────────────────
USE_RAG=false                        # Enable curriculum context
CHUNK_SIZE=500                       # Characters per chunk
CHUNK_OVERLAP=50                     # Overlap between chunks
TOP_K_CHUNKS=3                       # Retrieved chunks to use

LANGUAGE SETTINGS:
──────────────────
LANGUAGE_CONFIDENCE_THRESHOLD=0.5    # Minimum confidence for detection
DEBUG=false                          # Enable debug logging

RECOMMENDED SETTINGS:
────────────────────
For Fast Responses:
  TEMPERATURE=0.5
  MAX_TOKENS=512
  USE_RAG=false

For Detailed Answers:
  TEMPERATURE=0.7
  MAX_TOKENS=1024
  USE_RAG=true

For Creative Analogies:
  TEMPERATURE=1.0
  MAX_TOKENS=1024
  USE_RAG=true

═══════════════════════════════════════════════════════════════════════════════
"""

TROUBLESHOOTING = """
🔧 TROUBLESHOOTING

PROBLEM: "API Key not configured" error
SOLUTION:
  1. Check .env file exists in project folder
  2. Verify API key is correct
  3. Ensure LLM_PROVIDER matches your key's provider
  4. Restart Python/Streamlit after editing .env

PROBLEM: "Language not detected properly"
SOLUTION:
  1. Mixed language input confuses detection
  2. Try asking in pure language (not Hinglish)
  3. Adjust LANGUAGE_CONFIDENCE_THRESHOLD in .env
  4. English is used as fallback

PROBLEM: "Slow responses"
SOLUTION:
  1. Free tier APIs may be rate-limited
  2. Try Groq (fastest free option)
  3. Reduce MAX_TOKENS in .env
  4. Disable RAG if not needed

PROBLEM: "ImportError: No module named 'streamlit'"
SOLUTION:
  1. Install dependencies: pip install -r requirements.txt
  2. Verify virtual environment is activated
  3. Try: pip install --upgrade streamlit

PROBLEM: "FAISS ImportError"
SOLUTION:
  1. Reinstall: pip install --force-reinstall faiss-cpu
  2. On Mac M1: pip install --upgrade faiss-cpu
  3. Ensure you're not trying faiss-gpu

═══════════════════════════════════════════════════════════════════════════════
"""

NEXT_STEPS = """
📚 NEXT STEPS

AFTER INSTALLATION:
───────────────────
1. Read README.md for feature overview
2. Check INSTALLATION.md if you face issues
3. Run test suite: python test_prototype.py
4. Try asking questions in different languages
5. Explore configuration options in sidebar

TO EXTEND THE SYSTEM:
──────────────────────
1. Add more analogies in analogy_engine.py
2. Add NCERT documents to data/ncert_docs/
3. Modify prompts in prompts.py for different tone
4. Add new languages in config.py
5. Read ARCHITECTURE.md for extension points

TO DEPLOY PROFESSIONALLY:
──────────────────────────
1. Use Docker: docker build -t bhaashaguru .
2. Deploy to Streamlit Cloud
3. Use environment variables for secrets
4. Set up CI/CD pipeline
5. Monitor API usage and costs

TO PREPARE FOR GPU DEPLOYMENT:
────────────────────────────────
1. Read ROCm section in README.md
2. Study GPU inference examples in backend.py
3. Prepare AMD GPU cluster
4. Plan model quantization strategy
5. Optimize for inference latency

═══════════════════════════════════════════════════════════════════════════════
"""

COMMAND_REFERENCE = """
🖥️ COMMON COMMANDS

INSTALLATION:
──────────────
pip install -r requirements.txt          # Install dependencies
python -m venv venv                      # Create virtual environment
source venv/bin/activate                 # Activate (Linux/macOS)
venv\\Scripts\\activate                   # Activate (Windows)

RUNNING:
────────
streamlit run app.py                     # Start web interface
python test_prototype.py                 # Run tests
python -c "from backend import..."       # Quick test

CONFIGURATION:
──────────────
cp .env.example .env                     # Create config file
nano .env                                # Edit config (macOS/Linux)
notepad .env                             # Edit config (Windows)

QUICK START (Auto):
────────────────────
bash quickstart.sh                       # Linux/macOS
quickstart.bat                           # Windows Command Prompt
.\\quickstart.ps1                         # Windows PowerShell

DEBUGGING:
──────────
DEBUG=true streamlit run app.py          # Enable debug logs
python -c "from langdetect import detect; print(detect('हेलो'))"
curl https://api.groq.com/ping           # Test API connectivity

═══════════════════════════════════════════════════════════════════════════════
"""

RESOURCES = """
📚 LEARNING RESOURCES

ABOUT BHAASHAGURU:
──────────────────
• README.md - Feature overview
• INSTALLATION.md - Setup guide
• ARCHITECTURE.md - Technical details
• FEATURES.md - Complete feature list

STREAMLIT:
───────────
• https://docs.streamlit.io/ - Official docs
• https://streamlit.io/gallery - Examples
• https://discuss.streamlit.io - Community

LLM PROVIDERS:
───────────────
• https://console.groq.com - Groq console
• https://huggingface.co - HuggingFace Hub
• https://openrouter.io - OpenRouter

NCERT RESOURCES:
─────────────────
• https://ncert.nic.in/ - Official NCERT site
• https://www.vedantu.com/ - Vedantu (curriculum)
• https://www.byju.com/ - BYJU'S (videos)

PYTHON LIBRARIES:
──────────────────
• langdetect - Language detection
• sentence-transformers - Text embeddings
• faiss-cpu - Vector search
• requests - HTTP client
• python-dotenv - Environment variables

GPU DEPLOYMENT (Future):
──────────────────────────
• https://rocmdocs.amd.com/ - AMD ROCm docs
• https://huggingface.co/docs/transformers - Transformers
• https://vllm.ai/ - vLLM inference

═══════════════════════════════════════════════════════════════════════════════
"""

print(SYSTEM_OVERVIEW)
print(QUICK_START)
print(PROJECT_STRUCTURE)
print(FILE_DESCRIPTIONS)
print(SUPPORTED_LANGUAGES)
print(LLM_PROVIDERS)
print(FEATURE_OVERVIEW)
print(USAGE_EXAMPLES)
print(CONFIGURATION_GUIDE)
print(TROUBLESHOOTING)
print(NEXT_STEPS)
print(COMMAND_REFERENCE)
print(RESOURCES)

print("""
═══════════════════════════════════════════════════════════════════════════════

🎉 YOU'RE READY TO GO!

1. Set up your environment:
   cp .env.example .env
   # Add your API key to .env

2. Start the app:
   streamlit run app.py

3. Ask questions in any language!

═══════════════════════════════════════════════════════════════════════════════
Built with ❤️ for Indian Students | Made for AMD ROCm Deployment
""")
