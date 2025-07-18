from gamestate import GameState

class UI:
    @staticmethod
    def welcome() -> None:
        """Welcomes the player to Casino"""
        print('\n\n***** Welcome to the casino *****\n')

    @staticmethod
    def get_start_game_input() -> str:
        """Asks if the player wants to play blackjack"""
        while True:
            print('\nStart a blackjack game? (y/n):')
            choice = input().strip().lower()

            if choice in ['y', 'n']:
                return choice
            print('Please enter y or n.')

    @staticmethod
    def show_player_balance(player: object) -> None:
        """Shows the balance of the player"""
        print(f"\nCurrent Balance: {player.balance}")

    @staticmethod
    def show_hands(player: object, dealer: object) -> None:
        """Shows the hidden dealer hand and complete player hand"""
        print(f"\nDealer | ** {' '.join(dealer.hand[1:])} |")
        print(f"Player | {' '.join(card for card in player.hand)} | {player.card_sum()}")

    @staticmethod
    def show_complete_hands(player: object, dealer: object) -> None:
        """Shows complete dealer and player hand"""
        print('\nDealer | ' + ' '.join(card for card in dealer.hand) + ' | ' + dealer.card_sum())
        print('Player | ' + ' '.join(card for card in player.hand) + ' | ' + player.card_sum())

    @staticmethod
    def get_bet_input(player: object) -> int:
        while True:
            print('\nHow much would you like to bet?: (q to exit)')
            bet = input().strip().lower()

            if bet == 'q':
                import sys
                sys.exit()

            try:
                bet_amount = int(bet)
                if bet_amount <= 0:
                    print('Please bet an amount greater than zero.')
                elif bet_amount > player.balance:
                    print(f"Your bet exceeds your current balance ${player.balance}")
                else:
                    return bet_amount
            except ValueError:
                print("Please enter a valid number.")

    @staticmethod
    def get_decision_input() -> str:
        while True:
            print('Would you like to double, hit, or stand (d, h, s): ')
            decision = input().strip().lower()

            if decision in ['d', 'h', 's']:
                return decision
            else:
                print('Please type a valid character')

    @staticmethod
    def display_message(message: str) -> None:
        print(message)

    @staticmethod
    def print_push(bet_amount: int) -> None:
        print(f"Push! Your initial bet of {bet_amount} has been returned to your account.")

    @staticmethod
    def print_blackjack(individual: str, bet_amount: int=None) -> None:
        print(f"{individual} blackjack!" + 'You lose!' if individual == 'Dealer'
              else f'A balance of + ${bet_amount * 1.5} has been added to your account')

    @staticmethod
    def print_bust(individual: str) -> None:
        print(f"{individual} busted!" + 'You win!' if individual == 'Dealer' else 'You lose!')

    @staticmethod
    def print_win(bet_amount: int) -> None:
        print(f"You win! a Balance of ${bet_amount * 2} has been added to your account.")

    @staticmethod
    def print_lose():
        print("You lose!")

    @staticmethod
    def print_out_of_money():
        print("\nYou are out of money :( See you again next time!")






