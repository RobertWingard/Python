class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'email: {self.email}')
        print(f'age: {self.age}')
        print(f'Member: {self.is_reward_member}')
        print(f'Points: {self.gold_card_points}')
        
    def enroll(self):
        if self.is_reward_member:
            print('User already a member.')
            return False


        self.is_reward_member = True
        self.gold_card_points = 100

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print('Whoa buddy... this purchase will take you in the nagative, and cant be processed. Please try again at a later date when you have updated your account with the appropriate amount of points.')
            return

        self.gold_card_points -= amount




user1 = User('Robert', 'Wingard', 'email.com', 34)
user2 = User('Stacy', 'Boots', "email.com", 33)
user3 = User('Mario', 'Brother', 'plumber@gmail.com', 53)
# user1.display_info()
user1.enroll()
user1.display_info()
user1.spend_points(50)
user1.display_info()
user2.enroll()
user2.display_info()
user2.spend_points(80)
user2.display_info()
user1.enroll()
user3.spend_points(200)
