import random

from responses import responses

class ChatBot:

    def __init__(self):

        self.name = "Nova"

    def get_response(self, user_input):
        user_input = user_input.lower().strip()

        # Greeting
        if user_input in ["hello", "hi", "hey"]:

            return random.choice(
                responses["greeting"]
            )
          
        # Asking bot condition
        elif "how are you" in user_input:

            return random.choice(
                responses["how_are_you"]
            )

        # Asking name
        elif "your name" in user_input:

            return random.choice(
                responses["name"]
            )

        # Thanks
        elif "thank" in user_input:

            return random.choice(
                responses["thanks"]
            )

        # Unknown input
        else:
            return "Sorry, I don't understand that yet."
