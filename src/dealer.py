from actor import Actor
from config import Config


class Dealer(Actor):
    def __init__(self):
        super().__init__()
        self.shoe = []

        # Creates the base deck based on the number of standard decks used
        for _ in range(Config.DECK_NUMBER):
            for s in Config.SUITS:
                for n in Config.NUMBERS:
                    self.shoe.append(s + n)

        self.ORIGINAL_DECK = self.shoe[:]

    # Reshuffles the deck by resetting it
    def reshuffle(self):
        if len(self.shoe) <= 0.25 * len(self.ORIGINAL_DECK):
            self.shoe = self.ORIGINAL_DECK[:]

    # Starts the game by dealing cards to the player and dealer
    def deal_card(self, player):
        # Deal player cards
        for _ in range(2):
            self.hit(player, self.shoe)
        # Deal dealer cards
        for _ in range(2):
            self.hit(self, self.shoe)

    # Hits cards on dealer based on the dealer rule
    def dealer_rule(self):
        while int(self.card_sum()) <= 16:
            self.hit(self, self.shoe)
