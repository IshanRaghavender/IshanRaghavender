# Enhanced Rule-Based Chatbot with Multiple Questions

def chatbot():
    print("Hello! I am a simple chatbot. Ask me anything or type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()  # Converts input to lowercase for easier matching
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking!")
        
        elif "your name" in user_input:
            print("Chatbot: I'm just a simple chatbot without a name. What would you like to call me?")
        
        elif "weather" in user_input:
            print("Chatbot: I can't access live weather data, but you can check a weather app for accurate information!")
        
        elif "time" in user_input:
            print("Chatbot: I can't tell time, but your device's clock should have the answer.")
        
        elif "favorite color" in user_input:
            print("Chatbot: I like all colors equally, but what's your favorite color?")
        
        elif "what can you do" in user_input:
            print("Chatbot: I can have simple conversations with you and answer basic questions.")
        
        elif "where are you from" in user_input:
            print("Chatbot: I exist in the digital world, created by code!")
        
        elif "who made you" in user_input:
            print("Chatbot: I was created by developers to demonstrate how chatbots work.")
        
        elif "tell me a joke" in user_input:
            print("Chatbot: Why don’t scientists trust atoms? Because they make up everything!")
        
        elif "who is the president" in user_input:
            print("Chatbot: I can't access live data, but a quick web search can tell you the current president.")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")

# Run the chatbot
chatbot()
