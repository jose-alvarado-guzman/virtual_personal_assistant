import yaml
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

class Dialect():

    def __init__(self, name):
        self.name = name
        self.train_conversation()

    def train_conversation(self):
        self.chatbot=ChatBot(self.name, logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.TimeLogicAdapter'])
        corpus_trainer = ChatterBotCorpusTrainer(self.chatbot)
        list_trainer = ListTrainer(self.chatbot)
        list_trainer.train(["What is your name?",
                            f'My name is {self.name}'
                            "What's your name?",
                            f'My name is {self.name}',
                            'How should I call you',
                            f'You can call me {self.name}',
                            'Do you have a name',
                            f'My name is {self.name}',
                           "I need your assistance",
                           "How can I help you today?",
                           "Goodbye Jarvis",
                           "Goodbye",
                           "Goodbye",
                           "Goodbye"
                           ])
        corpus_trainer.train("chatterbot.corpus.english.greetings",
                      "chatterbot.corpus.english.conversations",
                      "chatterbot.corpus.english.botprofile")

    def get_response(self, message):
        return self.chatbot.get_response(message)
