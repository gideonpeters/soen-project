from datetime import datetime

class Chat:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username in self.users:
            return False
        self.users[username] = []
        return True

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        return False

    def send_message(self, sender, receiver, message):
        if sender not in self.users or receiver not in self.users:
            return False
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_data = {'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp}
        self.users[sender].append(message_data)
        self.users[receiver].append(message_data)
        return True

    def get_messages(self, username):
        if username in self.users:
            return self.users[username]
        return []

if __name__ == '__main__':
    unittest.main()
