import re
RULES = [
    (["hello", "hi", "hey"], "Hello! How can I help you?"),
    (["name"], "I am a simple AI chatbot."),
    (["how are you"], "I am fine. Thank you for asking!"),
    (["course", "subject"], "I can provide basic information about your course."),
    (["help"], "Sure! You can ask me about my name, course, or general information."),
    (["thank", "thanks"], "You are welcome!"),
]
EXIT_PATTERNS = ["bye", "exit", "quit"]
EXIT_RESPONSE = "Goodbye! Have a nice day."
DEFAULT_RESPONSE = "Sorry, I do not understand your question."
def matches(patterns, text):
    for p in patterns:
        if re.search(r"\b" + re.escape(p) + r"\b", text):
            return True
    return False
def get_response(user_input):
    text = user_input.lower().strip()
    if matches(EXIT_PATTERNS, text):
        return EXIT_RESPONSE, True
    for patterns, response in RULES:
        if matches(patterns, text):
            return response, False
    return DEFAULT_RESPONSE, False
def main():
    print("Chatbot: Welcome! Type 'bye', 'exit' or 'quit' to end the chat.")
    while True:
        user_input = input("User: ")
        response, should_exit = get_response(user_input)
        print("Chatbot:", response)
        if should_exit:
            break
if __name__ == "__main__":
    main()