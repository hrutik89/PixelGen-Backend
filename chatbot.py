import openai

openai.api_key = "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"

def generate_chat(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
