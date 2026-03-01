#!/usr/bin/env python3
"""
Test Script for BhaashaGuru
Tests the system with multilingual STEM questions
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

import backend
from backend import generate_explanation


def test_hindi_math():
    """Test Hindi math question."""
    print("\n" + "="*80)
    print("TEST 1: Hindi Math Question")
    print("="*80)
    
    question = "वर्ग समीकरण x² + 5x + 6 = 0 को हल करने का तरीका समझाएं।"
    print(f"Question: {question}\n")
    
    result = generate_explanation(question, mode="full")
    
    print(f"Language Detected: {result['language_name']} (Confidence: {result['language_confidence']:.1%})")
    print(f"Mode: {'Hint' if result['mode'] == 'hint' else 'Full Explanation'}")
    print(f"\nResponse:\n{result['response']}")
    
    if result.get('analogy'):
        print(f"\nAnalogy: {result['analogy']}")


def test_tamil_physics():
    """Test Tamil physics question."""
    print("\n" + "="*80)
    print("TEST 2: Tamil Physics Question")
    print("="*80)
    
    question = "நியூட்டனின் இரண்டாவது இயக்க விதியை விளக்குங்கள்."
    print(f"Question: {question}\n")
    
    result = generate_explanation(question, mode="full")
    
    print(f"Language Detected: {result['language_name']} (Confidence: {result['language_confidence']:.1%})")
    print(f"Mode: {'Hint' if result['mode'] == 'hint' else 'Full Explanation'}")
    print(f"\nResponse:\n{result['response']}")
    
    if result.get('analogy'):
        print(f"\nAnalogy: {result['analogy']}")


def test_telugu_hint():
    """Test Telugu with hint mode."""
    print("\n" + "="*80)
    print("TEST 3: Telugu Chemistry Question (Hint Mode)")
    print("="*80)
    
    question = "రసాయన సమీకరణలను సమతుల్యం చేయడం ఎలా?"
    print(f"Question: {question}\n")
    
    result = generate_explanation(question, mode="hint")
    
    print(f"Language Detected: {result['language_name']} (Confidence: {result['language_confidence']:.1%})")
    print(f"Mode: {'Hint' if result['mode'] == 'hint' else 'Full Explanation'}")
    print(f"\nResponse:\n{result['response']}")
    
    if result.get('analogy'):
        print(f"\nAnalogy: {result['analogy']}")


def test_bengali_biology():
    """Test Bengali biology question."""
    print("\n" + "="*80)
    print("TEST 4: Bengali Biology Question")
    print("="*80)
    
    question = "সালোকসংশ্লেষণ প্রক্রিয়া ব্যাখ্যা করুন।"
    print(f"Question: {question}\n")
    
    result = generate_explanation(question, mode="full")
    
    print(f"Language Detected: {result['language_name']} (Confidence: {result['language_confidence']:.1%})")
    print(f"Mode: {'Hint' if result['mode'] == 'hint' else 'Full Explanation'}")
    print(f"\nResponse:\n{result['response']}")
    
    if result.get('analogy'):
        print(f"\nAnalogy: {result['analogy']}")


def test_english():
    """Test English question."""
    print("\n" + "="*80)
    print("TEST 5: English Question")
    print("="*80)
    
    question = "What is the Pythagorean theorem and how is it used?"
    print(f"Question: {question}\n")
    
    result = generate_explanation(question, mode="full")
    
    print(f"Language Detected: {result['language_name']} (Confidence: {result['language_confidence']:.1%})")
    print(f"Mode: {'Hint' if result['mode'] == 'hint' else 'Full Explanation'}")
    print(f"\nResponse:\n{result['response']}")
    
    if result.get('analogy'):
        print(f"\nAnalogy: {result['analogy']}")


def main():
    """Run all tests."""
    print("\n" + "="*80)
    print("BhaashaGuru - Prototype Testing Suite")
    print("="*80)
    print("\nConfiguration:")
    print(f"- Provider: {backend.config.PROVIDER.upper()}")
    print(f"- Model: {backend.config.MODEL_NAME}")
    print(f"- Temperature: {backend.config.TEMPERATURE}")
    print(f"- RAG Enabled: {backend.config.USE_RAG}")
    
    try:
        # Run tests
        test_hindi_math()
        test_tamil_physics()
        test_telugu_hint()
        test_bengali_biology()
        test_english()
        
        print("\n" + "="*80)
        print("✅ All tests completed successfully!")
        print("="*80)
    
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure your API key is configured in .env file")
        print("2. Check that you're connected to the internet")
        print("3. Verify the LLM_PROVIDER setting matches your API")
        print("4. See .env.example for configuration template")
        sys.exit(1)


if __name__ == "__main__":
    main()
