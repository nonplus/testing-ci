def respond(user_input):
    if "What is your name?" == user_input:
        return "My name is chatbot! What's yours?"
    else:
        return "Sorry I didn't understand that."

def main():
    while True:
        user_input = input()
        response = respond(user_input)
        print(response)

if __name__ == '__main__':
    main()
