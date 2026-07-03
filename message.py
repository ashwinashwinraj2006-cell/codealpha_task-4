# ============================================================
# TASK 4: Basic Rule-Based Chatbot
# Key Concepts: if-elif, functions, loops, input/output
# ============================================================

# ── Predefined responses dictionary ─────────────────────────
RESPONSES = {
    # Greetings
    "hello":          "Hi there! 😊 How can I help you today?",
    "hi":             "Hey! Great to see you. What's up?",
    "hey":            "Hey hey! What can I do for you?",
    "good morning":   "Good morning! ☀️ Hope you have a wonderful day!",
    "good afternoon": "Good afternoon! 🌤️ How's your day going?",
    "good evening":   "Good evening! 🌙 How can I assist you?",

    # How are you
    "how are you":         "I'm doing great, thanks for asking! 😄 How about you?",
    "how are you doing":   "I'm running smoothly and ready to chat! How are you?",
    "what's up":           "Not much! Just here to help you. What's on your mind?",
    "how do you do":       "I do quite well, thank you! How can I assist?",

    # About the bot
    "what is your name":   "I'm ChatBot 🤖, your simple virtual assistant!",
    "what are you":        "I'm a rule-based chatbot built with Python. Ask me anything!",
    "who are you":         "I'm ChatBot — a friendly Python-powered assistant! 🐍",
    "are you a robot":     "Yes! I'm a bot, but I promise I'm a friendly one. 🤖",
    "are you human":       "Nope! I'm 100% Python code. But I try my best to be helpful!",

    # Help
    "help":                "Sure! You can ask me: greetings, how I'm doing, jokes, time, or just say bye!",
    "what can you do":     "I can chat, tell jokes, and keep you company. Try saying 'tell me a joke'!",

    # Jokes
    "tell me a joke":      "Why don't scientists trust atoms? Because they make up everything! 😄",
    "joke":                "Why did the programmer quit his job? Because he didn't get arrays! 😂",
    "funny":               "I told my computer I needed a break... now it won't stop sending me Kit-Kat ads! 🍫",

    # Thanks
    "thank you":           "You're welcome! 😊 Happy to help.",
    "thanks":              "Anytime! That's what I'm here for. 🙌",
    "thanks a lot":        "My pleasure! Let me know if you need anything else.",

    # Feelings
    "i am sad":            "I'm sorry to hear that. 😢 Remember, every storm runs out of rain. 🌈",
    "i am happy":          "That's awesome! 😄 Happiness looks great on you!",
    "i am bored":          "Let's fix that! Want to hear a joke? Just type 'joke'!",
    "i am tired":          "Take a break and rest up! 💤 I'll be here when you're back.",
    "i am fine":           "Glad to hear it! 😊 Keep it up!",

    # Farewell
    "bye":                 "Goodbye! 👋 Take care and have a great day!",
    "goodbye":             "See you later! 😊 It was nice chatting with you!",
    "see you":             "See you soon! 👋 Come back anytime.",
    "exit":                "Exiting chat... Goodbye! 👋",
    "quit":                "Quitting chat... Take care! 😊",
}

# Keywords that signal the user wants to exit
EXIT_KEYWORDS = {"bye", "goodbye", "exit", "quit", "see you"}


def clean_input(user_text):
    """
    Normalize user input:
    - Strip leading/trailing whitespace
    - Convert to lowercase
    - Remove trailing punctuation
    """
    text = user_text.strip().lower()
    text = text.rstrip("!?.,")
    return text


def get_response(user_input):
    """
    Match the cleaned user input against the RESPONSES dictionary.
    Returns a matching reply or a default fallback message.
    """
    cleaned = clean_input(user_input)

    # ── Exact match first ────────────────────────────────────
    if cleaned in RESPONSES:
        return RESPONSES[cleaned]

    # ── Partial / keyword match ──────────────────────────────
    for key, reply in RESPONSES.items():
        if key in cleaned:
            return reply

    # ── Fallback response ────────────────────────────────────
    return "🤔 Hmm, I didn't quite understand that. Try saying 'help' to see what I can do!"


def is_exit(user_input):
    """Return True if the user wants to end the conversation."""
    cleaned = clean_input(user_input)
    return cleaned in EXIT_KEYWORDS


def print_banner():
    """Display a welcome banner when the chatbot starts."""
    print("\n" + "=" * 50)
    print("       🤖  WELCOME TO CHATBOT v1.0  🤖")
    print("=" * 50)
    print("  Type a message and press Enter to chat.")
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'quit' to exit.")
    print("=" * 50 + "\n")


def chat():
    """Main chat loop — keeps running until the user says goodbye."""
    print_banner()
    print("  ChatBot : Hi! I'm ChatBot 🤖. How can I help you?\n")

    while True:
        try:
            user_input = input("  You     : ").strip()
        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C or Ctrl+D gracefully
            print("\n  ChatBot : Goodbye! 👋 (Session ended)\n")
            break

        # Skip empty input
        if not user_input:
            print("  ChatBot : Please type something! I'm listening. 👂\n")
            continue

        # Get and display response
        response = get_response(user_input)
        print(f"  ChatBot : {response}\n")

        # Exit if user said bye/quit/etc.
        if is_exit(user_input):
            break


# ─── MAIN ───────────────────────────────────────────────────
if __name__ == "__main__":
    chat()
