import ai21
import pywhatkit
import tkinter as tk

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

    # For now, let's just print the user's message
    print("User:", message)
    # print(a['completions'][0]['data']['text'])
    print((f"bot:{a['completions'][0]['data']['text']} "))
    # Clear the input field
    entry.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Chat Bot Interface")

# Create a text area to display the chat messages
text_area = tk.Text(window, height=20, width=50)
text_area.pack()

# Create an entry field for the user's input
entry = tk.Entry(window, width=50)
entry.pack()

# Create a button to send the message
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start the main event loop
window.mainloop()







# a = ai21.Completion.execute(
#   model="j2-grande-instruct",
#   prompt= 'give python programing motivation',
#   numResults=1,
#   maxTokens=500,
#   temperature=0.7,
#   topKReturn=0,
#   topP=1,
#   countPenalty={
#     "scale": 0,
#     "applyToNumbers": False,
#     "applyToPunctuations": False,
#     "applyToStopwords": False,
#     "applyToWhitespaces": False,
#     "applyToEmojis": True
#   },
#   frequencyPenalty={
#       "scale": 0,
#       "applyToNumbers": False,
#       "applyToPunctuations": False,
#       "applyToStopwords": False,
#       "applyToWhitespaces": False,
#       "applyToEmojis": False
#   },
#   presencePenalty={
#       "scale": 0,
#       "applyToNumbers": False,
#       "applyToPunctuations": False,
#       "applyToStopwords": False,
#       "applyToWhitespaces": False,
#       "applyToEmojis": False
#   },
#   stopSequences=[]
# )

# print(a['prompt']['text'])
# print(a)
# print(a['completions'][0]['data']['text'])
# pywhatkit.sendwhatmsg("+972549889177",a['completions'][0]['data']['text'], 15, 35, 15, True, 2)
# pywhatkit.sendwhatmsg_to_group(, a['completions'][0]['data']['text'], 23,55)
# lst = ["+972549889177", "+972538253297", "+972559771087" ]
# for i in lst:
#     pywhatkit.sendwhatmsg_instantly(i,a['completions'][0]['data']['text'])

# pywhatkit.sendwhatmsg_instantly("+972549889177",a['completions'][0]['data']['text'])







