"""
BhaashaGuru - Multilingual STEM Tutoring System
Streamlit UI for the BhaashaGuru backend
"""
import streamlit as st
import backend
import config
from typing import Optional
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="BhaashaGuru",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #FF6B35;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .response-box {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF6B35;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
        color: #ffffff;
    }
    .error-box {
        background: linear-gradient(135deg, #3d1a1a 0%, #4d2a2a 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff6666;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
        color: #ffffff;
    }
    .hint-box {
        background: linear-gradient(135deg, #3d2d1a 0%, #4d3d2a 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FFB84D;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
        color: #ffffff;
    }
    .language-badge {
        display: inline-block;
        background-color: #FF6B35;
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: bold;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables."""
    if "history" not in st.session_state:
        st.session_state.history = []
    if "last_response" not in st.session_state:
        st.session_state.last_response = None


def display_header():
    """Display the main header."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="main-header">🧠 BhaashaGuru</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">Multilingual STEM Tutor for Indian Students</div>', unsafe_allow_html=True)


def display_sidebar_config():
    """Display configuration options in sidebar."""
    st.sidebar.markdown("## ⚙️ Configuration")
    
    # RAG toggle
    use_rag = st.sidebar.checkbox(
        "📖 Use NCERT Curriculum Context (RAG)",
        value=config.USE_RAG,
        help="Enable retrieval of relevant NCERT content"
    )
    
    # Temperature slider
    temperature = st.sidebar.slider(
        "🔥 Temperature (Creativity)",
        min_value=0.0,
        max_value=2.0,
        value=config.TEMPERATURE,
        step=0.1,
        help="Higher = more creative, Lower = more focused"
    )
    
    # Model info
    st.sidebar.markdown("### 📚 Model Information")
    st.sidebar.info(f"""
    **Provider**: {config.PROVIDER.upper()}
    
    **Model**: {config.MODEL_NAME}
    
    **Max Tokens**: {config.MAX_TOKENS}
    """)
    
    return use_rag, temperature


def display_language_info(response_data: dict):
    """Display language detection info."""
    col1, col2 = st.columns([1, 2])
    
    with col1:
        language_badge = f'<span class="language-badge">{response_data["language_name"]}</span>'
        st.markdown(language_badge, unsafe_allow_html=True)
    
    with col2:
        confidence_percent = response_data["language_confidence"] * 100
        st.caption(f"Confidence: {confidence_percent:.1f}%")


def display_response(response_data: dict, use_rag: bool = False):
    """Display the response from the backend."""
    
    if not response_data.get("success", False):
        st.markdown(
            f'<div class="error-box">❌ **Error**: {response_data.get("error", "Unknown error")}</div>',
            unsafe_allow_html=True
        )
        return
    
    # Language info
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### 🌐 Detected Language")
        display_language_info(response_data)
    
    with col2:
        if response_data["mode"] == "hint":
            st.markdown("### 💡 Mode")
            st.info("Hint Mode")
        else:
            st.markdown("### 📚 Mode")
            st.info("Full Explanation")
    
    # Main response
    st.markdown("### 📝 Response")
    response_class = "hint-box" if response_data["mode"] == "hint" else "response-box"
    st.markdown(
        f'<div class="{response_class}">{response_data["response"]}</div>',
        unsafe_allow_html=True
    )
    
    # Analogy section
    if response_data.get("analogy"):
        st.markdown("### 🎯 Regional Analogy")
        st.success(response_data["analogy"])
    
    # RAG indicator
    if use_rag and response_data.get("rag_used"):
        st.info("📖 This response was enhanced with NCERT curriculum context.")


def get_speech_input():
    """Create a voice input component using Web Speech API."""
    html_code = """
    <html>
    <head>
        <style>
            .voice-container {
                text-align: center;
                padding: 20px;
            }
            .voice-btn {
                background: linear-gradient(135deg, #FF6B35, #FF8555);
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 25px;
                font-size: 16px;
                cursor: pointer;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(255, 107, 53, 0.4);
            }
            .voice-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(255, 107, 53, 0.6);
            }
            .voice-btn:active {
                transform: translateY(0);
            }
            .recording {
                background: linear-gradient(135deg, #ff4444, #ff6666);
                animation: pulse 1.5s infinite;
            }
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
            .transcript-box {
                margin-top: 15px;
                padding: 10px;
                background-color: #f0f0f0;
                border-radius: 8px;
                min-height: 30px;
                font-size: 14px;
                color: #333;
            }
            .listening-indicator {
                color: #FF6B35;
                font-weight: bold;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="voice-container">
            <button class="voice-btn" id="voiceBtn" onclick="toggleVoiceInput()">🎤 Click to Record</button>
            <div class="transcript-box" id="transcript"></div>
            <div class="listening-indicator" id="indicator"></div>
        </div>

        <script>
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            let isListening = false;

            recognition.continuous = false;
            recognition.interimResults = true;
            recognition.lang = 'en-IN';

            function toggleVoiceInput() {
                if (!isListening) {
                    startListening();
                } else {
                    stopListening();
                }
            }

            function startListening() {
                isListening = true;
                const btn = document.getElementById('voiceBtn');
                const indicator = document.getElementById('indicator');
                const transcript = document.getElementById('transcript');
                
                btn.classList.add('recording');
                btn.textContent = '🎤 Listening...';
                indicator.textContent = '🔴 Recording...';
                transcript.textContent = '';
                
                recognition.start();
            }

            function stopListening() {
                isListening = false;
                recognition.stop();
            }

            recognition.onresult = function(event) {
                let interimTranscript = '';
                let finalTranscript = '';

                for (let i = event.resultIndex; i < event.results.length; i++) {
                    const transcript = event.results[i][0].transcript;
                    if (event.results[i].isFinal) {
                        finalTranscript += transcript + ' ';
                    } else {
                        interimTranscript += transcript;
                    }
                }

                document.getElementById('transcript').textContent = finalTranscript || interimTranscript;
            };

            recognition.onend = function() {
                isListening = false;
                const btn = document.getElementById('voiceBtn');
                const indicator = document.getElementById('indicator');
                btn.classList.remove('recording');
                btn.textContent = '🎤 Click to Record';
                indicator.textContent = '';
            };

            recognition.onerror = function(event) {
                const transcript = document.getElementById('transcript');
                transcript.textContent = 'Error: ' + event.error;
                transcript.style.color = '#ff0000';
            };
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=200)


def display_help_section():
    """Display help information."""
    with st.expander("❓ How to Use BhaashaGuru"):
        st.markdown("""
        ### Welcome to BhaashaGuru!
        
        **BhaashaGuru** is your multilingual STEM tutor supporting Indian regional languages.
        
        #### Supported Languages:
        - 🇮🇳 हिन्दी (Hindi)
        - 🇮🇳 தமிழ் (Tamil)
        - 🇮🇳 తెలుగు (Telugu)
        - 🇮🇳 বাংলা (Bengali)
        - 🇮🇳 मराठी (Marathi)
        - 🇮🇳 ગુજરાતી (Gujarati)
        - 🇮🇳 ಕನ್ನಡ (Kannada)
        - 🇮🇳 മലയാളം (Malayalam)
        - 🇬🇬 English
        
        #### Features:
        1. **Auto Language Detection**: Automatically detects your language
        2. **Step-by-Step Explanations**: Learn concepts systematically
        3. **Hint Mode**: Get a nudge without the full answer
        4. **Cultural Analogies**: Relatable examples in your language
        5. **NCERT Integration**: Optional curriculum-aware responses
        
        #### How to Use:
        1. Type your STEM question in any supported language
        2. Choose between "Explain" (full) or "Give Hint" (guided)
        3. Adjust settings in the sidebar if needed
        4. Read the step-by-step response
        5. Use analogies to understand concepts better
        
        #### Example Questions:
        - "वर्ग समीकरण को हल करने का तरीका बताएं"
        - "பித்தாகोரஸ் సిద్ధాంతం ఏమిటి?"
        - "How do I balance a chemical equation?"
        """)


def main():
    """Main Streamlit application."""
    init_session_state()
    display_header()
    
    # Sidebar configuration
    use_rag, temperature = display_sidebar_config()
    
    # Help section
    display_help_section()
    
    # Main input section
    st.markdown("## 📝 Ask Your Question")
    
    # Text input section only
    st.markdown("### 📝 Enter Your Question")
    col1, col2 = st.columns([3, 1])
    with col1:
        question = st.text_area(
            label="Your STEM Question",
            placeholder="Enter your question in any Indian language or English...",
            height=120,
            label_visibility="collapsed"
        )
    with col2:
        st.markdown("### Mode")
        mode = st.radio(
            label="Select mode",
            options=["Explain", "Give Hint"],
            label_visibility="collapsed"
        )
    
    # Convert mode to backend format
    backend_mode = "full" if mode == "Explain" else "hint"
    
    # Buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        submit_button = st.button(
            f"🚀 {mode}",
            use_container_width=True,
            type="primary"
        )
    
    with col2:
        clear_button = st.button(
            "🗑️ Clear",
            use_container_width=True
        )
    
    with col3:
        st.empty()
    
    # Handle button clicks
    if clear_button:
        st.session_state.last_response = None
        st.rerun()
    
    if submit_button:
        if not question.strip():
            st.error("❌ Please enter a question first!")
        else:
            # Show loading state
            with st.spinner("🤔 Thinking... (This may take a moment)"):
                try:
                    # Generate response
                    response_data = backend.generate_explanation(
                        question=question,
                        mode=backend_mode,
                        use_rag=use_rag
                    )
                    
                    # Store in session state
                    st.session_state.last_response = response_data
                    st.session_state.history.append({
                        "question": question,
                        "mode": backend_mode,
                        "response": response_data
                    })
                
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
                    st.info("💡 Make sure your API key is configured correctly in environment variables.")
    
    # Display last response
    if st.session_state.last_response:
        st.markdown("---")
        st.markdown("## 📖 Response")
        display_response(st.session_state.last_response, use_rag)
    
    # Display history
    if st.session_state.history:
        with st.expander(f"📚 Conversation History ({len(st.session_state.history)} items)"):
            for i, item in enumerate(st.session_state.history, 1):
                st.markdown(f"**Question {i}**: {item['question']}")
                st.markdown(f"*Mode*: {'Full Explanation' if item['mode'] == 'full' else 'Hint'}")
                if st.button(f"View Answer {i}", key=f"history_{i}"):
                    st.session_state.last_response = item['response']
                    st.rerun()
                st.divider()


if __name__ == "__main__":
    main()
