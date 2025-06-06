#Class = Thirdy's Circle 
#Class = Friends
#Attributes = name, nickname, favorite memory, input no. of friends
#Methods = user input, summary, no. of friends

class ThirdyCircle():
    def __init__(self, name, nickname, fav_memo):
        self.name = name 
        self.nickname = nickname 
        self.fav_memo = fav_memo 

class Friends():
    def __init__(self):
        self.friends = []
        
    def add_friends_function(self):
        self.name = input("\nEnter name: ")
        self.nickname = input("Enter nickname: ")
        self.fav_memo = input("Favorite Memory: ")
        add_friends = ThirdyCircle(self.name, self.nickname, 
                                   self.fav_memo)
        self.friends.append(add_friends)
    
    def show_friends(self):
        for friend in self.friends:
            print(f"\nName: {friend.name}")
            print(f"Nickname: {friend.nickname}")
            print(f"{friend.fav_memo} is my favorite memory.")

show_thirdy_circle = Friends()
        
no_of_friends = int(input("Enter number of friends: "))
for i in range(no_of_friends):
    show_thirdy_circle.add_friends_function() 

show_thirdy_circle.show_friends()
    
        