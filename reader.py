import csv
from typing import Any


def load_strategy(filename: str) -> dict[Any, Any]:
    strategy = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)[1:]
        # print(f"[DEBUG] Strategy file {filename} headers: {headers}")

        for row in reader:
            player_sum = row[0]
            strategy[player_sum] = dict(zip(headers, row[1:]))

        # print(f"[DEBUG] Strategy keys: {list(strategy.keys())}")
        return strategy


HARD_HAND_STRATEGY = load_strategy("data/hard_total.csv")
SOFT_HAND_STRATEGY = load_strategy("data/soft_total.csv")


def normalize_card(card):
    # Handle both raw ranks and card strings with suits
    if isinstance(card, str) and len(card) > 2:
        # Extract rank from card string like "♦Q" -> "Q"
        card = normalize_rank(card)

    if card in {'10', 'J', 'Q', 'K'}:
        return 'KQJ'  # Changed back to match CSV headers
    return card


def normalize_rank(card):
    # Extract rank from card string like "♦Q" -> "Q"
    # Remove all non-alphanumeric characters and return the rank
    import re
    rank = re.sub(r'\W', '', card)
    return rank if rank else card


def hand_value(ranks):
    total = 0
    aces = ranks.count('A')

    for r in ranks:
        if r in {'K', 'Q', 'J'}:
            total += 10
        elif r != 'A':
            try:
                total += int(r)
            except ValueError:
                print(f"[ERROR] Could not convert rank '{r}' to integer")
                # Skip invalid ranks
                continue

    # Add aces
    for _ in range(aces):
        total += 11 if total + 11 <= 21 else 1
    return total


def is_soft_hand(ranks):
    if 'A' not in ranks:
        return False
    hard_sum = hand_value([r for r in ranks if r != 'A'])
    return hard_sum + 11 <= 21


def get_action(player_hand, dealer_card):
    ranks = [normalize_rank(card) for card in player_hand]
    dealer_card = normalize_card(dealer_card)

    # print(f"[DEBUG] Player hand: {player_hand} -> ranks: {ranks}")
    # print(f"[DEBUG] Dealer card: {dealer_card}")

    if is_soft_hand(ranks):
        non_ace = [r for r in ranks if r != 'A']

        if not non_ace:
            key = 'A2'
        else:
            key = 'A' + non_ace[0]

        # print(f"[DEBUG] Soft hand key: {key}")
        action = SOFT_HAND_STRATEGY.get(key, {}).get(dealer_card, 'H')
        # print(f"[DEBUG] Soft hand action: {action}")
        return action.lower()
    else:
        total = str(hand_value(ranks))
        # print(f"[DEBUG] Hard hand total: {total}")
        action = HARD_HAND_STRATEGY.get(total, {}).get(dealer_card, 'H')
        # print(f"[DEBUG] Hard hand action: {action}")
        return action.lower()
