import requests

response = requests.post("http://localhost:11434/api/generate", json={
  "model": "llama2",
  "prompt": "用一句话介绍 Ollama"
})

for line in response.iter_lines():
    if line:
        print(line.decode("utf-8"))