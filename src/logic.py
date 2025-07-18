from ui import UI


class GameLogic:
    pass


class Logic:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.IN_GAME = True
        self.IN_ROUND = True
        self.BUST = False

    def welcome(self) -> None:
        UI.welcome()
        if UI.get_start_game_input() == 'n':
            self.IN_GAME = False

    def bet(self):
        UI.show_player_balance(self.player)
        bet_amount = UI.get_bet_input(self.player)
        self.player.bet_amount = bet_amount
        self.player.subtract_balance(bet_amount)

    def deal(self):
        """Dealer deals cards to both player and dealer"""
        self.dealer.deal_card(self.player)

    def dealer_rule(self):
        self.dealer.dealer_rule()

    def show_balance(self):
        UI.show_player_balance(self.player)

    def show_hands(self):
        UI.show_hands(self.player, self.dealer)

    def show_complete_hands(self):
        UI.show_complete_hands(self.player, self.dealer)

    def decisions(self):
        self.player.turn += 1
        decision = UI.get_decision_input()

        if decision == 'd':
            self.player.hit(self.player, self.dealer.shoe)
            self.player.subtract_balance(self.player.bet_amount)
            self.player.bet_amount *= 2
            self.IN_ROUND = False
        elif decision == 'h':
            self.player.hit(self.player, self.dealer.shoe)
            # Check if player busted, if bust end game
            if self.player.bust():
                self.player.isbust = True
                self.IN_ROUND = False
        elif decision == 's':
            self.IN_ROUND = False

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

        # Check for blackjack
        if player_blackjack and dealer_blackjack:
            self.dealer.blackjack = True
            self.player.blackjack = True
            self.show_complete_hands()
            UI.print_push(self.player.bet_amount)
            self.player.add_balance(self.player.bet_amount)
        elif dealer_blackjack:
            self.dealer.blackjack = True
            self.show_complete_hands()
            UI.print_blackjack(individual='Dealer')
        elif player_blackjack:
            self.player.blackjack = True
            self.show_complete_hands()
            UI.print_blackjack(individual='Player', bet_amount=self.player.bet_amount)
            self.player.add_balance(self.player.bet_amount * 2.5)

    def check_bust(self):
        # Check if player busted
        if self.player.isbust:
            UI.show_complete_hands(self.player, self.dealer)
            UI.print_bust('You')
            self.BUST = True
        # Check if dealer busted
        elif self.dealer.bust():
            UI.show_complete_hands(self.player, self.dealer)
            UI.print_bust('Dealer')
            self.player.add_balance(self.player.bet_amount * 2)
            self.BUST = True

    def check_winner(self):
        player_sum = int(self.player.card_sum())
        dealer_sum = int(self.dealer.card_sum())

        if player_sum > dealer_sum:
            UI.print_win(self.player.bet_amount)
            self.player.add_balance(self.player.bet_amount * 2)
        elif player_sum < dealer_sum:
            UI.print_lose()
        else:
            UI.print_push(self.player.bet_amount)
            self.player.add_balance(self.player.bet_amount)

    def reshuffle(self):
        self.dealer.reshuffle()

    def reset(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.IN_ROUND = True
        self.BUST = False

    def check_balance(self):
        if self.player.balance <= 0:
            UI.print_out_of_money()
            self.IN_GAME = False