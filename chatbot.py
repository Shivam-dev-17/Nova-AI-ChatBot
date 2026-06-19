import random

from responses import responses, intents

from nlp_engine import tokenize

class ChatBot:

    def __init__(self):

        self.name="Nova"

    def get_response(self,user_input):

        words = tokenize(user_input)

        message = " ".join(words)


        for intent, examples in intents.items():


            for example in examples:


                if example in message:


                    return random.choice(
                        responses[intent]
                    )

        return "Sorry, I don't understand that yet."
