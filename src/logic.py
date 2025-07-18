from ui import UI
from gamestate import GameState


class Logic:
    def __init__(self, player, dealer):
        """Initializes the logic."""
        self.player = player
        self.dealer = dealer

    def welcome(self) -> None:
        """Welcome to the game."""
        UI.welcome()
        if UI.get_start_game_input() == 'n':
            GameState.end_game()

    def bet(self) -> None:
        """Asks player to bet."""
        UI.show_player_balance(self.player)
        bet_amount = UI.get_bet_input(self.player)
        self.player.bet_amount = bet_amount
        self.player.subtract_balance(bet_amount)

    def deal(self) -> None:
        """Dealer deals cards to both player and dealer."""
        self.dealer.deal_card(self.player)

    def dealer_rule(self) -> None:
        """Deal card to dealer based on dealer rules."""
        self.dealer.dealer_rule()

    def show_balance(self) -> None:
        """Shows player's balance."""
        UI.show_player_balance(self.player)

    def show_hands(self) -> None:
        """Shows player's and hidden dealer's hands."""
        UI.show_hands(self.player, self.dealer)

    def show_complete_hands(self) -> None:
        """Shows player's and dealer's hands."""
        UI.show_complete_hands(self.player, self.dealer)

    def decisions(self) -> None:
        """Asks for player's decision."""
        self.player.turn += 1
        decision = UI.get_decision_input()

        if decision == 'd':
            self.player.hit(self.player, self.dealer.shoe)
            self.player.subtract_balance(self.player.bet_amount)
            self.player.bet_amount *= 2
            GameState.end_round()
        elif decision == 'h':
            self.player.hit(self.player, self.dealer.shoe)
            # Check if player busted, if bust end round
            if self.player.bust():
                self.player.isbust = True
                GameState.end_round()
        elif decision == 's':
            GameState.end_round()

    def check_blackjack(self) -> None:
        """Checks blackjack for player and dealer."""
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

    def check_bust(self) -> None:
        """Checks if player or dealer busts."""
        # Check if player busted
        if self.player.isbust:
            UI.show_complete_hands(self.player, self.dealer)
            UI.print_bust('You')
            GameState.bust = True
        # Check if dealer busted
        elif self.dealer.bust():
            UI.show_complete_hands(self.player, self.dealer)
            UI.print_bust('Dealer')
            self.player.add_balance(self.player.bet_amount * 2)
            GameState.bust = True

    def check_winner(self) -> None:
        """Check if player or dealer wins."""
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

    def reshuffle(self) -> None:
        """Reshuffles deck."""
        self.dealer.reshuffle()

    def reset(self) -> None:
        """Resets game conditions."""
        self.player.reset_hand()
        self.dealer.reset_hand()
        GameState.start_new_round()

    def check_balance(self) -> None:
        """Checks player's balance."""
        if self.player.balance <= 0:
            UI.print_out_of_money()
            GameState.end_game()