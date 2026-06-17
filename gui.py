import tkinter as tk

from chatbot import ChatBot

class ChatBotGUI:

    def __init__(self):

        self.bot = ChatBot()
        
        self.window = tk.Tk()

        self.window.title("Nova AI Assistant")

        self.window.geometry("500x600")

        self.chat_box = tk.Text(
            self.window,
            height=25,
            width=60
        )

        self.chat_box.pack(
            padx=10,
            pady=10
        )

        self.user_input = tk.Entry(
            self.window,
            width=40
        )

        self.user_input.pack(
            side=tk.LEFT,
            padx=10,
            pady=10
        )

        self.send_button = tk.Button(
            self.window,
            text="Send",
            command=self.send_message
        )

        self.send_button.pack(
            side=tk.RIGHT,
            padx=10
        )

        self.window.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    def send_message(self):
        message = self.user_input.get()
        if message.strip() == "":

            return

        self.chat_box.insert(
            tk.END,
            "You: " + message + "\n"
        )
        response = self.bot.get_response(message)

        self.chat_box.insert(
            tk.END,
            "Nova: " + response + "\n\n"
        )

        self.user_input.delete(
            0,
            tk.END
        )

    def start(self):

        self.window.mainloop()
