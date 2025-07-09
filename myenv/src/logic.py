from player import Player
from dealer import Dealer


class Logic():
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.IN_WHOLE_GAME = True
        self.IN_GAME = True
        self.BUST = False
        
        
    def welcome(self):
        # Welcomes the player to Casino
        print("\n\n****** Welcome to the casino ******\n")
        
       
        while True:
            # Asks if the player wants to play blackjack
            start_game = input("Start a blackjack game? (y/n): ")
        
            if start_game.lower() == 'n':
                print("See you next time!")
                self.IN_WHOLE_GAME = False
                break
            elif start_game.lower() == 'y':
                print("Ok! Let's get started!")
                break
            else:
                print("Please type a vaild chracter\n")
            
            
    def bet(self):
        # Prints current balance and asks for amount to bet
        print(f"\nCurrent Balance: ${self.player.money}")
        self.player.bet()
        
        
    def deal(self):
        # Dealer deals cards to both Player and Delaer
        self.dealer.deal_card(self.player)
        
        
    def show_balance(self):
        # Show current player balance
        print(f"\nCurrent Balance: ${self.player.money}")
        
        
    def show_hands(self):
        # Shows hidden dealer hand and complete Player hand
        print('\nDealer | ** ' + ' '.join(self.dealer.hand[1:]) + ' | ?')        
        print('Player | ' + ' '.join(card for card in self.player.hand) + ' | ' + self.player.card_sum())
        
        
    def show_complete_hands(self):
        # Shows complete Dealer and Player hand
        print('\nDealer | ' + ' '.join(card for card in self.dealer.hand) + ' | ' + self.dealer.card_sum())
        print('Player | ' + ' '.join(card for card in self.player.hand) + ' | ' + self.player.card_sum())

        
    def decisions(self):
        player_decision = input("Would you like to double, hit, or stand? (d, h, s): ")
        
        if player_decision.lower() == 'd':
            self.player.hit(self.player, self.dealer.shoe)
            self.player.subtract_balance(self.player.bet_amount)
            self.player.bet_amount *= 2
            self.IN_GAME = False
            
        elif player_decision.lower() == 'h':
            self.player.hit(self.player, self.dealer.shoe)
            # Check if the player busted
            # If the player busts, end the game
            if self.player.bust():
                self.IN_GAME = False
                
        elif player_decision.lower() == 's':
            self.IN_GAME = False
        
        
    def check_bust(self):
        # Check if player busted
        if self.player.isbust:
            print('\nDealer | ' + ' '.join(card for card in self.dealer.hand) + ' | ' + self.dealer.card_sum())
            print('Player | ' + ' '.join(card for card in self.player.hand) + ' | ' + self.player.card_sum())
            print('You busted! You lose.')
            self.BUST = True
        # Check if dealer busted
        elif self.player.isbust:
            print('\nPlayer | ' + ' '.join(card for card in self.player.hand) + ' | ' + self.player.card_sum())
            print('Player | ' + ' '.join(card for card in self.player.hand) + ' | ' + self.player.card_sum())
            print('Dealer busted! You win')
            self.BUST = True

        
    def check_winner(self):
        if int(self.player.card_sum()) > int(self.dealer.card_sum()):
            print(f"You win! A balance of ${self.player.bet_amount * 2} has been added to your account")
            self.player.add_balance(self.player.bet_amount*2)
        elif int(self.player.card_sum()) < int(self.dealer.card_sum()):
            print(f"You lost!")
        else:
            print(f"Push! Your initial bet of ${self.player.bet_amount} has been returned to your account")
            self.player.add_balance(self.player.bet_amount)

    
    def reshuffle(self):
        self.dealer.reshuffle()
    
    
    def reset(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.IN_GAME = True
        self.BUST = False
        
        
    def check_balance(self):
        if self.player.money <= 0:
            print('\nYou are out of money :( See you again next time!')
            self.IN_WHOLE_GAME = False