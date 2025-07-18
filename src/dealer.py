import numbers

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
        super().__init__()
        self.shoe = []

        # Creates the base deck based on the number of standard decks used
        for _ in range(Config.DECK_NUMBER):
            for suit in Suit:
                for number in Number:
                    self.shoe.append(suit.value + number.value)

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
