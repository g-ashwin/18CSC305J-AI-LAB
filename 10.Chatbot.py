import random

responses={
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm doing well, thank you.",
    "what's your name": "My name is Chatbot.",
    "what can you do": "I can have simple conversations with you!",
    "goodbye": "Goodbye, have a great day!",
}
def get_response(message):
    message=message.lower()
    if message in responses:
        return responses [message]
    else:
        return "I'm sorry, I don't understand what you're saying."

def run_chatbot():
    print("Hello! I'm a simple conversation AI chatbot. You can say 'goodbye' to exit.")
    while True:
        message=input("You: ") 
        if message=="goodbye":
             print(get_response(message)) 
             break
        else:
             print("Chatbot:", get_response(message))
                
run_chatbot()
