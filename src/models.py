class AppModel:
    def __init__(self):
        self.message = "Welcome to Page 1"

    def get_message(self):
        return self.message

    def set_message(self, new_message):
        self.message = new_message
