import tkinter as tk
import random

# --- Simple rule-based chatbot logic ---
def get_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey", "yo"]
    how_are_you = ["how are you", "how are you doing", "what's up"]
    goodbye = ["bye", "goodbye", "see ya", "exit"]

    if any(word in user_input for word in greetings):
        return random.choice(["Hey there! 👋", "Hi! How can I help you? 😊", "Yo! 🔥"])
    elif any(phrase in user_input for phrase in how_are_you):
        return random.choice(["I'm doing great! You? 💫", "Feeling awesome! What about you? 😎"])
    elif any(word in user_input for word in goodbye):
        return "Catch you later! 👋"
    elif "your name" in user_input:
        return "I'm your Python buddy chatbot 😄"
    elif "love" in user_input:
        return "Awww, love you too 💖"
    elif "help" in user_input:
        return "Sure, I'm here to help! Just ask me something 🧠"
    elif "joke" in user_input:
        return random.choice([
            "Why don’t skeletons fight each other? They don’t have the guts. 💀",
            "What’s a computer’s favorite snack? Microchips. 😎",
            "404 joke not found 😬"
        ])
    else:
        return random.choice([
            "Hmm, interesting 🤔",
            "Can you say that differently?",
            "I’m not sure I got that… try rephrasing?",
            "Tell me more! 👀"
        ])

# --- GUI Setup ---
def send_message():
    user_msg = entry.get()
    if not user_msg.strip():
        return

    chat_window.insert(tk.END, f"You: {user_msg}\n")
    entry.delete(0, tk.END)

    bot_msg = get_response(user_msg)
    chat_window.insert(tk.END, f"Bot: {bot_msg}\n\n")
    chat_window.see(tk.END)

# --- Main GUI Window ---
root = tk.Tk()
root.title("Vibey Chatbot 9000 💬")
root.geometry("500x600")
root.configure(bg="#F0F8FF")

# Chat display area
chat_window = tk.Text(root, bg="#FFFFFF", fg="#333333", font=("Segoe UI", 11))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input field
entry = tk.Entry(root, font=("Segoe UI", 12))
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.focus()

# Send button
send_button = tk.Button(root, text="Send ✉️", command=send_message, font=("Segoe UI", 12), bg="#4CAF50", fg="white")
send_button.pack(pady=(0, 10))

# Allow Enter key to send
root.bind('<Return>', lambda event: send_message())

# Start GUI loop
root.mainloop()
