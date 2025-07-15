class Logic:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.IN_WHOLE_GAME = True
        self.IN_GAME = True
        self.BUST = False
        
        
    def welcome(self):
        # Welcomes the player to Casino
        print("\n\n****** Welcome to the casino ******\n", flush=True)
        
        while True:
            # Asks if the player wants to play blackjack
            print("Start a blackjack game? (y/n):")
            start_game = input().strip()
        
            if start_game.lower() == 'n':
                print("See you next time!")
                self.IN_WHOLE_GAME = False
                break
            elif start_game.lower() == 'y':
                print("Ok! Let's get started!")
                break
            else:
                print("Please type a valid character\n")
            
            
    def bet(self):
        # Prints current balance and asks for amount to bet
        print(f"\nCurrent Balance: ${self.player.money}")
        self.player.bet()
        
        
    def deal(self):
        # Dealer deals cards to both Player and Dealer
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
        self.player.turn += 1
        
        # CHANGE STRING TO "WOULD YOU LIKE TO DOUBLE, HIT, STAND, OR SPLIT (D, H, S, SPLIT)" ONCE SPLITTING IS IMPLEMENTED
        print("Would you like to double, hit, or stand (d, h, s): ")
        player_decision = input().strip()
        
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
                self.player.isbust = True
                self.IN_GAME = False
        elif player_decision.lower() == 's':
            self.IN_GAME = False
        elif player_decision.lower() == 'split':
            if self.player.hand[0][1:] != self.player.hand[1][1:]:
                print("Splitting is not allowed on your hand")
            # WORKING ON SPLITTING
            else:
                pass
        else:
            print("Please type a valid character")
            
        
    def check_blackjack(self):
        player_numbers = [card[1:] for card in self.player.hand]
        dealer_numbers = [card[1:] for card in self.dealer.hand]
        
        player_blackjack = (
            'A' in player_numbers and
            any(face in player_numbers for face in ['10', 'J', 'Q', 'K'])
        )
        
        dealer_blackjack = (
            'A' in dealer_numbers and
            any(face in dealer_numbers for face in ['10', 'J', 'Q', 'K'])
        )
        
        #Check for blackjack
        if player_blackjack and dealer_blackjack:
            self.dealer.blackjack = True
            self.player.blackjack = True
            self.show_complete_hands()
            print(f"Push! Your initial bet of ${self.player.bet_amount} has been returned to your account")
        elif dealer_blackjack:
            self.dealer.blackjack = True
            self.show_complete_hands()
            print(f"Dealer blackjack! You lose!")
        elif player_blackjack:
            self.player.blackjack = True
            self.show_complete_hands()            
            print(f"Blackjack! A balance of ${self.player.bet_amount * 1.5} has been added to your account")
            self.player.add_balance(self.player.bet_amount*1.5)
        
        
           
    
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
            print(f"You lose!")
        else:
            print(f"Push! Your initial bet of ${self.player.bet_amount} has been returned to your account")
            self.player.add_balance(self.player.bet_amount)

    
    def reshuffle(self):
        self.dealer.reshuffle()
    
    
    def reset(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.player.blackjack = False
        self.dealer.blackjack = False
        self.IN_GAME = True
        self.BUST = False
        self.player.turn = 1
        
        
    def check_balance(self):
        if self.player.money <= 0:
            print('\nYou are out of money :( See you again next time!')
            self.IN_WHOLE_GAME = False