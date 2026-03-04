# 8-11
send_messages = ["Hi", "Good morning", "Good evening"]
sent_messages = []

while send_messages :
    current_message = send_messages.pop()
    print(f"Sending message: {current_message}")
    sent_messages.append(current_message)

    print("\nThe following messages have been send:")
    for sent_message in sent_messages:
        print(sent_message) 

# 8-11

def print_messages(send_messages, sent_messages):

#print each message and move it to send_message list.

    while message:
        current_message = messages.pop(0)
        print(f"sending message : {current_message}")
        send_messages.append(current_message)

messages = ["Hi", "Good morning", "Good evening"]
sent_messages = []

sent_messages(messages.copy(), send_messages)
print("\noriginal list (unchanges):", messages)
print("Sent messages:", sent_messages)

