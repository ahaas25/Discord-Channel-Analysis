class User:
    def __init__ (self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.number_messages = 1    # Start with one, as user only added if spoken in channel


class Channel:
    messages = 0
    user_array = []

    def __init__(self, user_array, messages):
        self.user_array = user_array
        self.messages = messages