from actor import Actor


class Player(Actor):
    IN_GAME = True
    
    def __init__(self, money):
        super().__init__()
        self.money = money
        self.bet_amount = 0
        
    def bet(self):
        while True:
            bet = input("\nHow much would you like to bet?: ")
            
            if bet.isalpha():
                print("Please type a valid character")
            else:
                self.bet_amount = int(bet)
            
                if self.bet_amount > self.money:
                    print(f"Your bet exceeds your current balance ${self.money}")
                else:
                    self.money -= self.bet_amount
                    break
            
    def add_balance(self, money_added):
        self.money += money_added