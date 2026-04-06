class User:
    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count = User.user_count + 1


user1 = User("Sayantan Banerjee")
user2 = User("DebasishGhosh")
user3 = User("Proloy Maity")
print(user2.username)
print(user3.username)
print(User.user_count)
