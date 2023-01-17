
class User:
    def __init__(self, username, iden):
        self.user = username
        self.id = iden
        self.follower = 0
        self.follwing = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User("Ebube", "001")
user_2 = User("Tola", "002")

user_1.follow(user_2)

# print(user_1.following)
# print(user_1.follower)