print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Chatbot: Hi there! 😊")

    elif user_input == "how are you":
        print("Chatbot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Chatbot: My name is PythonBot.")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day 👋")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
