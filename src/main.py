from player import Player
from dealer import Dealer
from logic import Logic
from config import Config


def main():
    player1 = Player()
    dealer = Dealer()
    game = Logic(player1, dealer)

    # Welcome the player
    game.welcome()

    while game.IN_GAME:
        # Ask for bet
        game.bet()

        # Deal the cards
        game.deal()

        # Show player balance
        game.show_balance()

        # LOOP: Player makes decision
        while game.IN_ROUND:
            # Check blackjack
            if game.player.turn == 1:
                game.check_blackjack()
                if game.player.blackjack or game.dealer.blackjack:
                    break

            # Show cards
            game.show_hands()

            # If stand -> break
            # If double -> hit and break
            # If bust -> break
            game.decisions()

        if not game.player.blackjack and not game.dealer.blackjack:

            if not game.player.isbust:
                # Dealer rule
                game.dealer_rule()
            # Check if player is bust first, then check if dealer is bust
            game.check_bust()

        # Check the winner
        if not game.BUST and not game.player.blackjack and not game.dealer.blackjack:
            # Show cards
            game.show_complete_hands()
            # Check the winner
            game.check_winner()

        game.reshuffle()
        game.check_balance()
        game.reset()


if __name__ == '__main__':
    main()