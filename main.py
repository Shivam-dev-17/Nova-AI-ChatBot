from chatbot import ChatBot

bot = ChatBot()

print("-"*40)
print("🤖 Nova AI Chatbot")
print("Type 'exit' to stop")
print("-"*40)

while True:
    user_input = input("\nYou: ")
    if user_input.lower()=="exit":
        print("Bot: Goodbye Folk!")
        break
    response = bot.get_response(user_input)
    print("Bot:", response)
