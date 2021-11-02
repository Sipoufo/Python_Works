class user:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.follower = 0
        self.following = 0
        # print("This is my first class")
        
    def follow(self, user):
        user.follower += 1
        self.following += 1
        
user1 = user("OO1","User_1")
user2 = user("OO2","User_2")

user1.follow(user2)

print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)