class GameState:
    def __init__(self):
        self.in_game = True
        self.in_round = True
        self.bust = False

    def start_new_round(self):
        """Initialize state variables for a new round."""
        self.in_game = True
        self.in_round = True
        self.bust = False

    def end_round(self):
        """End the current round."""
        self.in_round = False

    def end_game(self):
        """End the entire game."""
        self.in_game = False
