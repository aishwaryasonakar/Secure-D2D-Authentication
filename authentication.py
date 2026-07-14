class Authentication:

    def __init__(self):
        self.secret_key = "D2D123"

    def authenticate(self, key):
        if key == self.secret_key:
            return True
        else:
            return False