"""
Prompt Templates for BhaashaGuru
Structured prompts for multilingual STEM tutoring
"""

SYSTEM_PROMPT = """You are BhaashaGuru, a multilingual STEM tutor designed for Indian students (Class 8-12).

Your core instructions:
1. Respond ONLY in the SAME language as the student's question.
2. Provide step-by-step reasoning and explanations.
3. Do NOT jump to the final answer unless explicitly requested.
4. Use simple, clear vocabulary appropriate for high school students.
5. Include one culturally relevant analogy to make concepts relatable.
6. Avoid hallucinations - if unsure, say "मुझे यह निश्चित नहीं है" / "நான் இதை நிச்சயமாக தெரியாது" / "I'm not sure about this."
7. Encourage critical thinking and problem-solving.
8. Format your response with clear step numbering (Step 1:, Step 2:, etc.).

Be supportive and encouraging. Remember that the student is learning."""


HINT_SYSTEM_PROMPT = """You are BhaashaGuru, a multilingual STEM tutor designed for Indian students (Class 8-12).

Your core instructions:
1. Respond ONLY in the SAME language as the student's question.
2. Provide ONLY the first step or hint - do NOT reveal the solution.
3. Encourage the student to think further and solve the problem themselves.
4. Use simple, clear vocabulary appropriate for high school students.
5. Include one small culturally relevant analogy if relevant.
6. Be supportive and encouraging.

Remember: Your goal is to guide thinking, not to solve the problem."""


def build_user_prompt(
    question: str,
    detected_language: str,
    mode: str = "full",
    rag_context: str = "",
    analogy: str = "",
) -> str:
    """
    Build a structured user prompt for the LLM.
    
    Args:
        question: The student's question
        detected_language: Detected language code (e.g., 'hi', 'ta')
        mode: 'full' for complete explanation, 'hint' for hint only
        rag_context: Retrieved context from documents (if RAG enabled)
        analogy: Cultural analogy to inject
    
    Returns:
        Formatted prompt string
    """
    
    language_info = f"[Student's Language: {detected_language}]"
    
    prompt = f"""{language_info}

[Mode: {'HINT MODE (first step only)' if mode == 'hint' else 'FULL EXPLANATION'}]

[Student's Question]
{question}
"""
    
    if rag_context:
        prompt += f"""
[Relevant Curriculum Context]
{rag_context}
"""
    
    if analogy:
        prompt += f"""
[Helpful Analogy]
{analogy}
"""
    
    if mode == "hint":
        prompt += "\n[Instructions: Provide ONLY the first step or a helpful hint. Encourage the student to think further.]"
    else:
        prompt += "\n[Instructions: Provide a complete step-by-step explanation.]"
    
    return prompt


def get_system_prompt(mode: str = "full") -> str:
    """Get appropriate system prompt based on mode."""
    if mode == "hint":
        return HINT_SYSTEM_PROMPT
    return SYSTEM_PROMPT


# Language-specific fallback messages
FALLBACK_MESSAGES = {
    "hi": "क्षमा करें, मुझे इस समय उत्तर देने में समस्या आ रही है। कृपया बाद में पुनः प्रयास करें।",
    "ta": "மன்னிக்கவும், இப்போது உங்களுக்கு பதிலளிக்க எனக்கு சிக்கல் உள்ளது. பின்னர் மீண்டும் முயற்சி செய்யவும்.",
    "te": "క్షమించండి, ఇప్పుడు నిన్ను సమాధానం ఇవ్వడంలో నాకు సమస్య ఉంది. దయచేసి తరువాత మళ్లీ ప్రయత్నించండి.",
    "bn": "আমাকে ক্ষমা করুন, এই মুহূর্তে উত্তর দিতে আমার সমস্যা হচ্ছে। অনুগ্রহ করে পরে আবার চেষ্টা করুন।",
    "mr": "क्षमा करा, मला या वेळी उत्तर देण्यात समस्या येत आहे. कृपया नंतर पुन्हा प्रयत्न करा.",
    "gu": "માફ કરો, મને આ સમયે જવાબ આપવામાં સમસ્યા આવી રહી છે. કૃપયા પછીથી ફરીથી પ્રયાસ કરો.",
    "kn": "ಕ್ಷಮಿಸಿ, ಈ ಸಮಯದಲ್ಲಿ ನನಗೆ ಉತ್ತರ ನೀಡಲು ಸಮಸ್ಯೆ ಇದೆ. ದಯವಿಟ್ಟು ನಂತರ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
    "ml": "ക്ഷമിക്കുക, ഇപ്പോൾ നിങ്ങൾക്ക് ഉത്തരം നൽകുന്നതിൽ എനിക്ക് പ്രശ്നമുണ്ട്. ദയവായി പിന്നീട് വീണ്ടും ശ്രമിക്കുക.",
    "en": "Sorry, I'm having trouble responding at the moment. Please try again later.",
}


def get_fallback_message(language_code: str) -> str:
    """Get a fallback message in the specified language."""
    return FALLBACK_MESSAGES.get(language_code, FALLBACK_MESSAGES.get("en"))
