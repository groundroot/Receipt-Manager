import urllib.request
import json
import os

api_key = os.environ.get('GEMINI_API_KEY', 'YOUR_KEY_HERE') # I won't have the user's key

payload = {
  "contents": [{
    "parts": [
      {"text": "이 영수증 이미지를 분석해서 아래 5가지 데이터를 JSON 형식으로 추출해줘...\n예시: {\"amount\": 15000, \"category\": \"식대 / 회식비\", \"date\": \"2023-10-25\", \"title\": \"스타벅스\", \"item_type\": \"서비스\"}"}
    ]
  }],
  "generationConfig": {"response_mime_type": "application/json"}
}
print("Test script created. Cannot test without user's API Key.")
