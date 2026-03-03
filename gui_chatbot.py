import tkinter as tk

def send_message():
    user_msg = entry_box.get().lower()
    entry_box.delete(0, tk.END)

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_msg + "\n")

    if user_msg == "hello":
        bot_reply = "Hi! How can I help you? 😊"
    elif user_msg == "how are you":
        bot_reply = "I'm doing great!"
    elif user_msg == "what is your name":
        bot_reply = "I'm Python GUI Bot 🤖"
    elif user_msg == "bye":
        bot_reply = "Goodbye! See you soon 👋"
    else:
        bot_reply = "Sorry, I didn't understand that."

    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

window = tk.Tk()
window.title("Python GUI Chatbot")
window.geometry("400x500")
window.resizable(False, False)

chat_area = tk.Text(window, bd=1, bg="white", font=("Arial", 12))
chat_area.place(x=6, y=6, height=385, width=370)
chat_area.config(state=tk.DISABLED)

entry_box = tk.Entry(window, bd=1, font=("Arial", 12))
entry_box.place(x=6, y=400, height=40, width=265)

send_button = tk.Button(
    window, text="Send", font=("Arial", 12),
    command=send_message
)
send_button.place(x=280, y=400, height=40, width=90)
window.bind("<Return>", lambda event: send_message())

window.mainloop()
