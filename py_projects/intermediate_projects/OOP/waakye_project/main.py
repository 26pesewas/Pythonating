class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0


user_one = User("2026", "Yellow")

print(user_one)
