import random

class Actor():
    
    def __init__(self):
        self.hand = []
        self.isbust = False
        self.win = False        
        
        
    # Resets the deck when starting a new game
    def reset_hand(self):
        self.hand = []
        self.isbust = False
        self.win = False


    # Deals a card to the individual and removes said card from base deck
    def hit(self, individual, deck):
        card = random.choice(deck)
        individual.hand.append(card)
        deck.remove(card)
    
    
    # Returns the sum of the cards as a string
    def card_sum(self):
        card_sum = 0
        a_count = 0
        
        for n in self.hand:
            if n[1:].isdigit():
                card_sum += int(n[1:])
            else:
                if n[1:] == 'A':
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
    
    
    # Checks if bust
    def bust(self):
        if int(self.card_sum()) > 21:
            self.isbust = True
            return True
        else:
            return False