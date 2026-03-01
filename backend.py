"""
Backend Core Logic for BhaashaGuru
Handles language detection, prompt building, LLM calls, and response formatting
"""
import config
import prompts
import analogy_engine
import rag
from typing import Dict, Tuple
import requests


def detect_language(text: str) -> Tuple[str, float]:
    """
    Detect language of input text using langdetect.
    
    Args:
        text: Input text
    
    Returns:
        Tuple of (language_code, confidence)
    """
    try:
        from langdetect import detect, detect_langs
        
        # Get all probabilities
        probabilities = detect_langs(text)
        
        # Find best match
        best_lang = None
        best_prob = 0
        
        for prob in probabilities:
            if prob.prob > best_prob:
                best_prob = prob.prob
                best_lang = prob.lang
        
        # Check confidence threshold
        if best_prob < config.LANGUAGE_CONFIDENCE_THRESHOLD:
            return (config.DEFAULT_LANGUAGE, best_prob)
        
        return (best_lang, best_prob)
    
    except Exception as e:
        print(f"[ERROR] Language detection failed: {e}")
        return (config.DEFAULT_LANGUAGE, 0.0)


def call_llm(
    system_prompt: str,
    user_prompt: str,
    temperature: float = None,
    max_tokens: int = None
) -> str:
    """
    Call LLM API and return response.
    
    Args:
        system_prompt: System instruction prompt
        user_prompt: User query prompt
        temperature: Generation temperature
        max_tokens: Maximum tokens to generate
    
    Returns:
        Generated response text
    """
    temperature = temperature or config.TEMPERATURE
    max_tokens = max_tokens or config.MAX_TOKENS
    
    try:
        if config.PROVIDER == "groq":
            return _call_groq(system_prompt, user_prompt, temperature, max_tokens)
        elif config.PROVIDER == "huggingface":
            return _call_huggingface(system_prompt, user_prompt, temperature, max_tokens)
        elif config.PROVIDER == "openrouter":
            return _call_openrouter(system_prompt, user_prompt, temperature, max_tokens)
        else:
            raise ValueError(f"Unknown provider: {config.PROVIDER}")
    
    except Exception as e:
        print(f"[ERROR] LLM call failed: {e}")
        raise


def _call_groq(system_prompt: str, user_prompt: str, temperature: float, max_tokens: int) -> str:
    """Call Groq API."""
    if not config.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not configured")
    
    headers = {
        "Authorization": f"Bearer {config.GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": config.MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_completion_tokens": max_tokens,
    }
    
    response = requests.post(config.API_ENDPOINT, json=payload, headers=headers, timeout=30)
    
    if response.status_code != 200:
        print(f"[ERROR] Groq API Error - Status: {response.status_code}")
        print(f"[ERROR] Response: {response.text}")
        print(f"[DEBUG] API Key: {config.GROQ_API_KEY[:20]}...")
        print(f"[DEBUG] Endpoint: {config.API_ENDPOINT}")
        print(f"[DEBUG] Model: {config.MODEL_NAME}")
    
    response.raise_for_status()
    
    result = response.json()
    return result["choices"][0]["message"]["content"]


def _call_huggingface(system_prompt: str, user_prompt: str, temperature: float, max_tokens: int) -> str:
    """Call HuggingFace Inference API."""
    if not config.HUGGINGFACE_API_KEY:
        raise ValueError("HUGGINGFACE_API_KEY not configured")
    
    headers = {
        "Authorization": f"Bearer {config.HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # HuggingFace expects a different message format
    combined_prompt = f"{system_prompt}\n\n{user_prompt}"
    
    payload = {
        "inputs": combined_prompt,
        "parameters": {
            "temperature": temperature,
            "max_new_tokens": max_tokens,
        }
    }
    
    url = config.API_ENDPOINT + config.MODEL_NAME
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    
    result = response.json()
    return result[0]["generated_text"]


def _call_openrouter(system_prompt: str, user_prompt: str, temperature: float, max_tokens: int) -> str:
    """Call OpenRouter API."""
    if not config.OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not configured")
    
    headers = {
        "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": config.MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    
    response = requests.post(config.API_ENDPOINT, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    
    result = response.json()
    return result["choices"][0]["message"]["content"]


def generate_explanation(
    question: str,
    language_code: str = None,
    mode: str = "full",
    use_rag: bool = None
) -> Dict:
    """
    Generate a complete explanation for a STEM question.
    
    Args:
        question: The student's question
        language_code: Detected language code (auto-detect if None)
        mode: 'full' or 'hint'
        use_rag: Whether to use RAG (uses config if None)
    
    Returns:
        Dictionary with response metadata and text
    """
    use_rag = use_rag if use_rag is not None else config.USE_RAG
    
    # Detect language if not provided
    if language_code is None:
        language_code, confidence = detect_language(question)
    else:
        confidence = 1.0
    
    # Get system prompt
    system_prompt = prompts.get_system_prompt(mode)
    
    # Get RAG context if enabled
    rag_context = ""
    if use_rag:
        rag_context = rag.retrieve_context(question)
    
    # Get analogy
    analogy = analogy_engine.get_random_analogy(language_code)
    
    # Build user prompt
    user_prompt = prompts.build_user_prompt(
        question=question,
        detected_language=language_code,
        mode=mode,
        rag_context=rag_context,
        analogy=analogy
    )
    
    try:
        # Call LLM
        response_text = call_llm(system_prompt, user_prompt)
        
        return {
            "success": True,
            "question": question,
            "detected_language": language_code,
            "language_name": analogy_engine.get_language_name(language_code),
            "language_confidence": confidence,
            "mode": mode,
            "response": response_text,
            "analogy": analogy,
            "rag_used": use_rag,
            "error": None
        }
    
    except Exception as e:
        error_msg = prompts.get_fallback_message(language_code)
        print(f"[ERROR] Generation failed: {e}")
        
        return {
            "success": False,
            "question": question,
            "detected_language": language_code,
            "language_name": analogy_engine.get_language_name(language_code),
            "language_confidence": confidence,
            "mode": mode,
            "response": error_msg,
            "analogy": None,
            "rag_used": use_rag,
            "error": str(e)
        }


def format_response_for_display(response_data: Dict) -> str:
    """
    Format response data for display in Streamlit.
    
    Args:
        response_data: Response dictionary from generate_explanation
    
    Returns:
        Formatted string for display
    """
    output = []
    
    # Language info
    output.append(f"🌐 **Detected Language**: {response_data['language_name']} (Confidence: {response_data['language_confidence']:.1%})")
    
    # Mode info
    if response_data['mode'] == 'hint':
        output.append("💡 **Mode**: Hint (First Step Only)")
    else:
        output.append("📚 **Mode**: Full Explanation")
    
    # Main response
    output.append("\n" + response_data['response'])
    
    # Analogy section if available
    if response_data.get('analogy'):
        output.append(f"\n🎯 **Regional Analogy**: {response_data['analogy']}")
    
    # RAG indicator
    if response_data['rag_used']:
        output.append("\n📖 *NCERT curriculum context was used in this response*")
    
    return "\n".join(output)


# Future Deployment Note:
# The LLM calls in this module (call_llm, _call_groq, etc.) are designed to be
# easily replaceable with local ROCm-enabled PyTorch model inference.
#
# To deploy on AMD GPU with ROCm:
# 1. Replace call_llm() to load model locally using ROCm-optimized PyTorch
# 2. Use vLLM or similar for efficient inference
# 3. Use models like Mistral-7B or Llama-3-8B with GPU acceleration
# 4. Keep the prompt engineering unchanged - it will work with any LLM
#
# Example ROCm replacement:
#   from transformers import AutoModelForCausalLM, AutoTokenizer
#   import torch
#   model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct")
#   model.to('rocm')
#   outputs = model.generate(inputs, max_new_tokens=config.MAX_TOKENS)
