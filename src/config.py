# Configure the constants in the blackjack game
import tomllib


class Config:
    with open("config.toml", 'rb') as f:
        config = tomllib.load(f)

    DECK_NUMBER = config['game']['deck_count']
    INITIAL_BALANCE = config['game']['initial_balance']
    BASE_BET = config['game']['base_bet']
