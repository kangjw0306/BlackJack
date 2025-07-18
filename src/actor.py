import random


class Actor:
    def __init__(self):
        """Initializes the actor."""
        self.hand = []
        self.isbust = False
        self.win = False
        self.turn = 1
        self.blackjack = False

    def reset_hand(self) -> None:
        """Reset the hand to its initial state."""
        self.hand = []
        self.isbust = False
        self.win = False
        self.blackjack = False
        self.turn = 1

    @staticmethod
    def hit(individual: object, deck: object) -> None:
        """Deals a card to the individual and removes said card from base deck"""
        card = random.choice(deck)
        individual.hand.append(card)
        deck.remove(card)

    def card_sum(self) -> str:
        """Calculates the sum of all cards in hand and returns it as a string."""
        card_sum = 0
        a_count = 0

        for n in self.hand:
            if n[1:].isdigit():
                card_sum += int(n[1:])
            elif n[1:] == 'A':
                a_count += 1
                card_sum += 11
            else:
                card_sum += 10

        for _ in range(a_count):
            if card_sum > 21:
                card_sum -= 10
            else:
                break

        return str(card_sum)

    def bust(self) -> bool:
        """Calculates if the hand is bust or not."""
        if int(self.card_sum()) > 21:
            self.isbust = True
            return True
        else:
            return False
