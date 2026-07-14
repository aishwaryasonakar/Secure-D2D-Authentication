class Logger:

    def log(self, message):

        with open("communication_log.txt", "a") as file:

            file.write(message + "\n")