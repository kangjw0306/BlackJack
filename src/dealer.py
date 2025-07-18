from actor import Actor
from config import Config
from enum import Enum


class Suit(Enum):
    CLUBS = '♣'
    DIAMONDS = '♦'
    HEARTS = '♥'
    SPADES = '♠'


class Number(Enum):
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'


class Dealer(Actor):
    def __init__(self):
        """Initializes the dealer."""
        super().__init__()
        self.shoe = []

        # Creates the base deck based on the number of standard decks used
        for _ in range(Config.DECK_NUMBER):
            for suit in Suit:
                for number in Number:
                    self.shoe.append(suit.value + number.value)

        self.ORIGINAL_DECK = self.shoe[:]

    def reshuffle(self) -> None:
        """Reshuffles the deck."""
        if len(self.shoe) <= 0.25 * len(self.ORIGINAL_DECK):
            self.shoe = self.ORIGINAL_DECK[:]

    def deal_card(self, player: object) -> None:
        """Deals cards to both the player and dealer."""
        for _ in range(2):
            self.hit(player, self.shoe)
        for _ in range(2):
            self.hit(self, self.shoe)

    def dealer_rule(self) -> None:
        """Hits cards on dealer based on dealer rules."""
        while int(self.card_sum()) <= 16:
            self.hit(self, self.shoe)
