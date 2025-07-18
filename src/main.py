from player import Player
from dealer import Dealer
from logic import Logic


def main():
    player1 = Player()
    dealer = Dealer()
    game = Logic(player1, dealer)

    game.welcome()

    while game.IN_GAME:
        game.bet()
        game.deal()
        game.show_balance()

        while game.IN_ROUND:
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

        if not game.BUST and not game.player.blackjack and not game.dealer.blackjack:
            game.show_complete_hands()
            game.check_winner()

        game.reshuffle()
        game.check_balance()
        game.reset()


if __name__ == '__main__':
    main()
