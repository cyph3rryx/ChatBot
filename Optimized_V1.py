import openai

def chatbot(prompt, api_key):
    try:
       
    
        message = completions.choices[0].text
        return message
    except Exception as e:
        print("Error in chatbot:", e)
        return None

while True:
    user_input = input("\nUser: ")
    if user_input == "exit":
        break

    response = chatbot(user_input, "YOUR-API")
    if response is not None:
        print("\nChatbot:", response)
    else:
        print("Error in chatbot")
