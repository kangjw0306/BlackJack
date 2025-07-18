from actor import Actor
from config import Config

class Player(Actor):
    IN_GAME = True

    def __init__(self, money=Config.INITIAL_BALANCE):
        """Initializes the player."""
        super().__init__()
        self.balance = money
        self.bet_amount = 0

    def subtract_balance(self, money_subtracted: int) -> None:
        """Subtracts money from balance."""
        self.balance -= money_subtracted

    def add_balance(self, money_added: int) -> None:
        """Adds money to balance."""
        self.balance += money_added
