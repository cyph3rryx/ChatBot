import openai

openai.api_key = "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"

def chatbot(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

while True:
    user_input = input("\nUser: ")
    if user_input == "exit":
        break

    response = chatbot(user_input)
    print("\nChatbot:", response)
