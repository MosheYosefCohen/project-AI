import ai21
import pywhatkit
import tkinter as tk
from tkinter import ttk

ai21.api_key = '0tdfIwigSDik6RmCGOBnmvR5k9SxXYda'


def send_message():
    message = entry.get()

    a = ai21.Completion.execute(
        model="j2-grande-instruct",
        prompt=message,
        numResults=1,
        maxTokens=500,
        temperature=0.7,
        topKReturn=0,
        topP=1,
        countPenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": True
        },
        frequencyPenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        presencePenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        stopSequences=[]
    )

    bot_response = f"bot: {a['completions'][0]['data']['text']}"

    text_area.configure(state='normal')
    text_area.insert(tk.END, f"\nUser: {message}\n\n")
    text_area.insert(tk.END, f"{bot_response}\n")
    text_area.configure(state='disabled')
    text_area.yview(tk.END)

    entry.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Chat Bot Interface")
window.geometry("600x800")

# Create a frame to hold the text area and the scrollbar
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Create a text area to display the chat messages
text_area = tk.Text(frame, wrap=tk.WORD, height=20, width=50, state='disabled')
text_area.grid(row=0, column=0, sticky=tk.NSEW)

# Create a scrollbar and associate it with the text area
scrollbar = ttk.Scrollbar(frame, command=text_area.yview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)
text_area['yscrollcommand'] = scrollbar.set

# Create an entry field for the user's input
entry = ttk.Entry(window, width=50)
entry.pack(padx=10, pady=10, fill=tk.X)

# Create a button to send the message
send_button = ttk.Button(window, text="Submit your question", command=send_message)
send_button.pack(padx=10, pady=5)

frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

# Start the main event loop
window.mainloop()


