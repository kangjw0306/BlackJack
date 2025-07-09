from actor import Actor

class Dealer(Actor):
    SUITS = ['♣', '♦', '♥', '♠']
    NUMBERS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    
    def __init__(self, deck_number):
        super().__init__()
        self.deck_number = deck_number
        self.shoe = []
        
        # Creates the base deck based on the number of standard decks used
        for _ in range(self.deck_number):
            for s in self.SUITS:
                for n in self.NUMBERS:
                    self.shoe.append(s + n)
        
        
        self.ORIGINAL_DECK = self.shoe[:]
            
                    
    # Reshuffles the deck by resetting it
    def reshuffle(self):
        if len(self.shoe) <= 0.25*len(self.ORIGINAL_DECK):
            self.shoe = self.ORIGINAL_DECK
    
    
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
        while self.card_sum() <= 16:
            self.hit(self, self.shoe)