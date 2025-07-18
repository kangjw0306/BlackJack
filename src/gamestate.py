class GameState:
    in_game = True
    in_round = True
    bust = False

    @staticmethod
    def start_new_round():
        """Initialize state variables for a new round."""
        GameState.in_game = True
        GameState.in_round = True
        GameState.bust = False

    @staticmethod
    def end_round():
        """End the current round."""
        GameState.in_round = False

    @staticmethod
    def end_game():
        """End the entire game."""
        GameState.in_game = False