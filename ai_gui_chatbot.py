import tkinter as tk
from openai import OpenAI

# ✅ Create OpenAI client
client = OpenAI(api_key="")

def send_message():
    user_msg = entry_box.get().strip()
    entry_box.delete(0, tk.END)

    if user_msg == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_msg + "\n")

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_msg
        )

        bot_reply = response.output_text

    except Exception as e:
        bot_reply = f"Error: {e}"

    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

# GUI window
window = tk.Tk()
window.title("AI Chatbot (ChatGPT Style)")
window.geometry("420x520")
window.resizable(False, False)

chat_area = tk.Text(window, bd=1, bg="white", font=("Arial", 12))
chat_area.place(x=6, y=6, height=400, width=400)
chat_area.config(state=tk.DISABLED)

entry_box = tk.Entry(window, bd=1, font=("Arial", 12))
entry_box.place(x=6, y=420, height=40, width=300)

send_button = tk.Button(window, text="Send", font=("Arial", 12), command=send_message)
send_button.place(x=315, y=420, height=40, width=90)

window.bind("<Return>", lambda event: send_message())

window.mainloop()

