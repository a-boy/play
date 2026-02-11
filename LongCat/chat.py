import requests

url = "https://api.longcat.chat/openai/chat/completions"
headers = {
    "Authorization": "Bearer ak_1of7ym6Ts7p77kC9dJ3Bn3j87t96K",
    "Content-Type": "application/json"
}

data = {
    "model": "LongCat-Flash-Chat",
    "messages": [
        {"role": "user", "content": "你好，请介绍一下htmx"}
    ],
    "max_tokens": 1000,
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
