from chatbot import ChatBot

bot=ChatBot()

print("-"*30)
print("🤖 Nova AI Chatbot")
print("Type 'exit' to Stop")
print("-"*30)

while True:
  user_input=input("\nYou: ")

if user_input.lower()=="exit":
  print("Bot: Goodbye Folk!")
  break
  
response = bot.get_response(user_input)

print("Bot:", response)
