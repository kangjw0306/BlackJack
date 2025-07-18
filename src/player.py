from actor import Actor
from config import Config

class Player(Actor):
    IN_GAME = True

    def __init__(self, money=Config.INITIAL_BALANCE):
        super().__init__()
        self.balance = money
        self.bet_amount = 0



    def subtract_balance(self, money_subtracted):
        self.balance -= money_subtracted

    def add_balance(self, money_added):
        self.balance += money_added
