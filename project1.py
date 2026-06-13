import datetime

vocabulary = {
    "hi":"hi there",
    "hello" : "hi there",
    "goodmorning" : "Oh , Hi , Good Morning to you too",
    "goodafternoon" : "Oh , Hi , Good Afternoon to you too",
    "goodevening" : "Oh , Hi , Good Evening to you too",
    "goodnight" : "Oh , Hi , Good Night to you too",
    "howareyou" : "I am fine , thank you",
    "name" : "I am a chatbot created by Aska , you can call me Ashy",
    "exit" : "Goodbye! Have a great day!",
    "goodbye" : "Goodbye! Have a great day!",
    "bye" : "Goodbye! Have a great day!",
    "thanks" : "You're welcome!",
    "thankyou" : "You're welcome!",
    "quit" : "Goodbye! Have a great day!"
    }
    
def response(clear_input):
    text = vocabulary.get(clear_input, "I'm sorry, I didn't understand that.")
    length = len(text)
    
    border = "+" + "-" * (length + 2) + "+"
    print()
    print(border)
    print(f"| {text} |")
    print(border)
    print()

def chatbot():
    while True:
        user_input = input("You: ")
        clear_input = user_input.lower().strip()
        clear_input = clear_input.replace("?", "").replace("!", "").replace(" ","")
        
        if clear_input in ["exit", "goodbye", "bye", "quit"]:
            response(clear_input)
            break
        else:
            response(clear_input)


chatbot()
