from actor import Actor
from config import Config
import sys

class Player(Actor):
    IN_GAME = True

    def __init__(self, money=Config.INITIAL_BALANCE):
        super().__init__()
        self.money = money
        self.bet_amount = 0

    def bet(self):
        while True:
            print("\nHow much would you like to bet?: (q to exit)")
            bet = input().strip()

            if bet == 'q':
                sys.exit()

            if bet.isalpha():
                print("Please type a valid character")
            elif int(bet) <= 0:
                print("Please bet an amount greater than $0")
            else:
                self.bet_amount = int(bet)

                if self.bet_amount > self.money:
                    print(f"Your bet exceeds your current balance ${self.money}")
                else:
                    self.money -= self.bet_amount
                    break

    def subtract_balance(self, money_subtracted):
        self.money -= money_subtracted

    def add_balance(self, money_added):
        self.money += money_added
