class Device:

    def __init__(self, name):
        self.name = name

    def connect(self):
        print(f"{self.name} is connected.")

    def send_message(self, message):
        print(f"{self.name} sends: {message}")

    def receive_message(self, message):
        print(f"{self.name} received: {message}")