from player import Player
from dealer import Dealer
from logic import Logic
from gamestate import GameState


def main():
    """Main function."""
    player1 = Player()
    dealer = Dealer()
    game = Logic(player1, dealer)

    game.welcome()

    # Debug: Print GameState attributes to diagnose missing in_game
    print("GameState attributes:", dir(GameState))

    while GameState.in_game:
        game.bet()
        game.deal()
        game.show_balance()

        while GameState.in_round:
            if game.player.turn == 1:
                game.check_blackjack()
                if game.player.blackjack or game.dealer.blackjack:
                    break

            game.show_hands()
            game.decisions()

        if not game.player.blackjack and not game.dealer.blackjack:
            if not game.player.isbust:
                game.dealer_rule()
            game.check_bust()

        if not GameState.bust and not game.player.blackjack and not game.dealer.blackjack:
            game.show_complete_hands()
            game.check_winner()

        game.reshuffle()
        game.check_balance()
        game.reset()


if __name__ == '__main__':
    main()