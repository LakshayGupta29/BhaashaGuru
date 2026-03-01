"""
Analogy Engine for BhaashaGuru
Injects culturally relevant regional analogies into explanations
"""
import random

# Regional analogies mapped by language
REGIONAL_ANALOGIES = {
    "hi": {
        "sports": [
            "क्रिकेट में रन बनाने की तरह, गणित में भी एक-एक स्टेप को ध्यान से समझना ज़रूरी है।",
            "जैसे खेती में बीज बोने से पहले जमीन तैयार करते हैं, वैसे ही विज्ञान में भी नींव मजबूत होनी चाहिए।",
        ],
        "culture": [
            "दिवाली की रोशनी की तरह, हर concept अपना महत्व रखता है।",
            "जैसे मंदिर की घंटी बजती है, वैसे ही हर प्रश्न का उत्तर है।",
        ],
        "nature": [
            "नदी की तरह, ज्ञान भी धीरे-धीरे बहता है।",
            "पेड़ की तरह, ज्ञान की जड़ें मजबूत होनी चाहिए।",
        ],
    },
    "ta": {
        "sports": [
            "கிரிக்கெட்டில் ரன் எடுக்கும் மாதிரி, கணிதத்திலும் ஒவ்வொரு படியை கவனமாக பார்க்க வேண்டும்.",
        ],
        "culture": [
            "கோவில் கட்டடக்கலை மாதிரி, விஞ்ஞானத்திலும் வடிவம் பெரிய பங்கு வகிக்கிறது.",
            "கோலம் என்ற கலை மாதிரி, கணிதமும் ஒரு அழகான வடிவத்தையே உண்டாக்குகிறது.",
        ],
        "nature": [
            "விவசாயம் மாதிரி, அறிவும் பொறுமையுடன் வளர்கிறது.",
        ],
    },
    "te": {
        "sports": [
            "కాయిట్‌లో వలె, భౌతిక శాస్త్రంలో కూడా ప్రతి పరిస్థితిని సూక్ష్మంగా విశ్లేషించాలి.",
        ],
        "culture": [
            "సంక్రాంతి పతంగ విసరినట్లు, విజ్ఞానం మనలను ఆకాశాలకు తీసుకెళుతుంది.",
            "ధాన్యం కోసిన ఆ విడిపోయిన పద్యం లాగా, రసాయన శాస్త్రం అణువుల లో నిపుణతను చూపుతుంది.",
        ],
    },
    "bn": {
        "sports": [
            "ক্রিকেটে যেমন প্রতিটি ডেলিভারি গুরুত্বপূর্ণ, গণিতেও প্রতিটি ধাপ অপরিহার্য।",
        ],
        "culture": [
            "দুর্গা পূজার মতো, বিজ্ঞানও একটি জটিল কিন্তু সুন্দর উদযাপন।",
            "নদীর খেয়াতুলির মতো, জ্ঞান আমাদের এক তীর থেকে অন্য তীরে নিয়ে যায়।",
        ],
    },
    "mr": {
        "sports": [
            "क्रिकेटमध्ये प्रत्येक चेंडू महत्त्वाचा असल्याप्रमाणे, गणितातही प्रत्येक पायरी महत्त्वाची आहे।",
        ],
        "culture": [
            "होळीच्या रंगांप्रमाणे, विज्ञान जीवनला रंगीत करते।",
        ],
    },
    "gu": {
        "culture": [
            "દિવાળીના દીયાઓની જેમ, આપણે જ્ઞાનના પ્રકાશ ફેલાવીએ છીએ।",
        ],
    },
    "kn": {
        "culture": [
            "ದಸರಾ ಉದ್ಯಾಪನೆಯ ಮತ್ತೆ, ಜ್ಞಾನವೂ ದುಷ್ಟತೆಯ ಮೇಲೆ ವಿಜಯ ಪಡೆಯುತ್ತದೆ.",
        ],
    },
    "ml": {
        "culture": [
            "ഈ ത്രിപുരാരിക്കായ ഭാഗവതംപോലെ, ഭൌതികശാസ്ത്രവും ഒരു ഗ്രന്ഥം പോലെ അദ്ഭുതകരം.",
        ],
    },
}


def get_random_analogy(language_code: str) -> str:
    """
    Get a random analogy for the specified language.
    
    Args:
        language_code: ISO 639-1 language code (e.g., 'hi', 'ta', 'te')
    
    Returns:
        A culturally relevant analogy string
    """
    # Get analogies for the language, or use Hindi as fallback
    analogies = REGIONAL_ANALOGIES.get(language_code, {})
    
    if not analogies:
        # Fallback to Hindi if language not found
        analogies = REGIONAL_ANALOGIES.get("hi", {})
    
    # Flatten all analogies
    all_analogies = []
    for category in analogies.values():
        all_analogies.extend(category)
    
    if all_analogies:
        return random.choice(all_analogies)
    
    # Ultimate fallback
    return "अभ्यास ही सफलता की कुंजी है। / Practice is the key to success."


def inject_analogy_into_prompt(prompt: str, analogy: str) -> str:
    """
    Inject an analogy into the prompt naturally.
    
    Args:
        prompt: The original prompt
        analogy: The analogy to inject
    
    Returns:
        Modified prompt with analogy
    """
    return f"{prompt}\n\nYou can use this analogy to help explain:\n{analogy}"


# Language name mappings
LANGUAGE_NAMES = {
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


def get_language_name(language_code: str) -> str:
    """Get native name of language from code."""
    return LANGUAGE_NAMES.get(language_code, language_code)
