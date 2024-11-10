import tkinter as tk

# Define chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "how are you?":
        return "I am a robot I have no feelings?"
    elif "how old are you?":
        return "I am robot I am not being old like human beings."
    elif "are you happy?":
        return "I hav eno feelings."
    else:
        return "I'm not sure how to respond to that yet."


# Function to handle user input and display response
def handle_response():
    user_input = user_input_entry.get()
    response = chatbot_response(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.insert(tk.END, "Chatbot: " + response + "\n")
    chat_log.config(state=tk.DISABLED)
    user_input_entry.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Graphical Chatbot")

# Create a canvas for drawing the chatbot face
canvas = tk.Canvas(root, width=200, height=200)
canvas.grid(row=0, column=0, columnspan=2)

# Draw the chatbot face (simple face with eyes and a mouth)
canvas.create_oval(50, 50, 150, 150, fill="lightblue")  # Face
canvas.create_oval(70, 80, 90, 100, fill="black")       # Left eye
canvas.create_oval(110, 80, 130, 100, fill="black")     # Right eye
canvas.create_line(80, 130, 120, 130, smooth=True)      # Mouth

# Create a text area to display the chat log
chat_log = tk.Text(root, width=50, height=10, state=tk.DISABLED)
chat_log.grid(row=1, column=0, columnspan=2)

# Entry widget for user input
user_input_entry = tk.Entry(root, width=40)
user_input_entry.grid(row=2, column=0)

# Button to send the message
send_button = tk.Button(root, text="Send", command=handle_response)
send_button.grid(row=2, column=1)

# Start the main event loop
root.mainloop()
