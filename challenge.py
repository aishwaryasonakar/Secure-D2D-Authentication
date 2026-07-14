import random

class Challenge:

    def generate(self):
        return random.randint(1000,9999)

    def verify(self, challenge, response):
        return challenge == response