import string
from datetime import datetime

BOT_NAME = "DecodeBot"

RESPONSES = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to see you.",
    "hey": "Hey! What's on your mind?",
    "good morning": "Good morning! Hope you have a great day.",
    "good evening": "Good evening! How can I help?",
    "how are you": "I'm just a bunch of if-else logic, but I'm running perfectly!",
    "what is your name": f"I'm {BOT_NAME}, a rule-based chatbot built at DecodeLabs.",
    "who are you": f"I'm {BOT_NAME}, your first deterministic AI assistant.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "what is ai": "Artificial Intelligence is the science of making machines perform tasks that normally need human intelligence.",
    "what is a rule based chatbot": "It's a bot that replies using predefined rules instead of learning from data.",
    "what is decodelabs": "DecodeLabs is the industrial training platform where interns build real-world AI projects.",
    "help": "Try: hello, how are you, what is ai, what is your name, time, or bye to exit.",
}

EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye", "q"}
FALLBACK = "Sorry, I do not understand that. Type 'help' to see what I can answer."


def sanitize(text):
    text = text.lower().strip().translate(str.maketrans("", "", string.punctuation))
    return " ".join(text.split())


def get_response(user_input):
    if user_input in ("time", "what time is it", "current time"):
        return "The time is " + datetime.now().strftime("%I:%M %p") + "."
    if user_input in ("date", "what is the date", "today"):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
    return RESPONSES.get(user_input, FALLBACK)


def main():
    print(f"{BOT_NAME}: Hello! Type 'help' for ideas or 'bye' to exit.")
    while True:
        try:
            user_input = sanitize(input("You: "))
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Goodbye!")
            break

        if not user_input:
            print(f"{BOT_NAME}: Please type something.")
            continue

        if user_input in EXIT_COMMANDS:
            print(f"{BOT_NAME}: Goodbye! Have a great day.")
            break

        print(f"{BOT_NAME}: {get_response(user_input)}")


if __name__ == "__main__":
    main()
