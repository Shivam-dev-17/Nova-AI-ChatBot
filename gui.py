import tkinter as tk
from tkinter import scrolledtext
from chatbot import ChatBot

class ChatBotGUI:

    def __init__(self):
        self.bot = ChatBot()

        self.window = tk.Tk()

        self.window.title("🤖 Nova AI Assistant")

        self.window.geometry("600x700")

        self.chat_box = scrolledtext.ScrolledText(
            self.window,
            height=30,
            width=70,
            wrap=tk.WORD
        )

        self.chat_box.pack(
            padx=10,
            pady=10
        )

        self.chat_box.config(
            state=tk.DISABLED
        )
        
        self.user_input = tk.Entry(
            self.window,
            width=50
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
            side=tk.LEFT
        )

        self.clear_button = tk.Button(
            self.window,
            text="Clear",
            command=self.clear_chat
        )

        self.clear_button.pack(
            side=tk.RIGHT,
            padx=10
        )

        self.window.bind(
            "<Return>",
            lambda event:self.send_message()
        )

        self.display_message(
            "Nova",
            "Hello! I am Nova, your AI assistant. How can I help you?"
        )

    def display_message(self, sender, message):

        self.chat_box.config(
            state=tk.NORMAL
        )

        self.chat_box.insert(
            tk.END,
            sender + ": " + message + "\n\n"
        )

        self.chat_box.config(
            state=tk.DISABLED
        )

        self.chat_box.yview(
            tk.END
        )

    def send_message(self):
        message = self.user_input.get()

        if message.strip()=="":
            return
            
        self.display_message(
            "You",
            message
        )

        response = self.bot.get_response(message)

        self.display_message(
            "Nova",
            response
        )

        self.user_input.delete(
            0,
            tk.END
        )

    def clear_chat(self):
        self.chat_box.config(
            state=tk.NORMAL
        )

        self.chat_box.delete(
            "1.0",
            tk.END
        )

        self.chat_box.config(
            state=tk.DISABLED
        )

    def start(self):
        self.window.mainloop()
