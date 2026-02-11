from anthropic import Anthropic

client = Anthropic(
    api_key="Authorization: Bearer ak_1of7ym6Ts7p77kC9dJ3Bn3j87t96K",
    base_url="https://api.longcat.chat/anthropic/",
    default_headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer ak_1of7ym6Ts7p77kC9dJ3Bn3j87t96K",
    }
)


response = client.messages.create(
    model="LongCat-Flash-Chat",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "How DLL works?"}
    ]
)

print(response.content[0].text)