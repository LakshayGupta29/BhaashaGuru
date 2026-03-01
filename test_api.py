#!/usr/bin/env python3
"""
Quick API Test Script
Tests Groq API connection
"""
import requests
import config

print("=" * 80)
print("BhaashaGuru - API Connection Test")
print("=" * 80)

print(f"\n✓ Provider: {config.PROVIDER}")
print(f"✓ API Key: {config.GROQ_API_KEY[:30]}...")
print(f"✓ Endpoint: {config.API_ENDPOINT}")
print(f"✓ Model: {config.MODEL_NAME}")

print("\n" + "=" * 80)
print("Testing Groq API Connection...")
print("=" * 80)

headers = {
    "Authorization": f"Bearer {config.GROQ_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": config.MODEL_NAME,
    "messages": [
        {"role": "user", "content": "Say hello in one word"}
    ],
    "temperature": 0.7,
    "max_completion_tokens": 10,
}

try:
    print("\nSending request to Groq API...")
    print(f"URL: {config.API_ENDPOINT}")
    print(f"Headers: {list(headers.keys())}")
    print(f"Payload: {payload}")
    
    response = requests.post(
        config.API_ENDPOINT,
        json=payload,
        headers=headers,
        timeout=10
    )
    
    print(f"\n✓ Status Code: {response.status_code}")
    print(f"✓ Response Headers: {dict(response.headers)}")
    print(f"\n📄 Full Response:\n{response.text}")
    
    if response.status_code == 200:
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        print(f"\n✅ SUCCESS! Response: {answer}")
    else:
        print(f"\n❌ ERROR: {response.status_code} - {response.text}")
        
except Exception as e:
    print(f"\n❌ Exception: {type(e).__name__}")
    print(f"❌ Error: {str(e)}")

print("\n" + "=" * 80)
