from openai import OpenAI

client = OpenAI(
    api_key="ak_1of7ym6Ts7p77kC9dJ3Bn3j87t96K",
    base_url="https://api.longcat.chat/openai"
)

response = client.chat.completions.create(
    model="LongCat-Flash-Chat",
    messages=[
        {"role": "user", "content": "Hello! Please introduce LongCat."}
    ],
    max_tokens=1000
)

print(response.choices[0].message.content)

'''
Hello! LongCat is an AI language model developed by Meituan, focused on providing users with intelligent and reliable conversational services. If you have any questions or need help, please feel free to ask me!
'''