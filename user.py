class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def make_deposit(self, amount):
        self.amount += amount
        
    def make_withdrawal(self,amount):
        self.amount -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.amount}")
        
    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount

user1 = User("Nathan Bludworth", 0.00)
user2 = User("Edward Smith", 0.00)
user3 = User("Peon Green", 0.00)

user1.make_deposit(200)
user1.make_deposit(100)
user1.make_deposit(300)
user1.make_withdrawal(400)
user1.display_user_balance()

user2.make_deposit(500)
user2.make_deposit(500)
user2.make_withdrawal(200)
user2.make_withdrawal(200)
user2.display_user_balance()

user3.make_deposit(1000)
user3.make_withdrawal(200)
user3.make_withdrawal(200)
user3.make_withdrawal(200)
user3.display_user_balance()

user1.transfer_money(user3, 100)
user1.display_user_balance()
user3.display_user_balance()