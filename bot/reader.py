import csv
import re
from typing import Any

def load_strategy(filename: str) -> dict[Any, Any]:
    strategy: dict[Any, Any] = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)[1:]

        for row in reader:
            player_sum = row[0]
            strategy[player_sum] = dict(zip(headers, row[1:]))

        return strategy

HARD_HAND_STRATEGY: dict[Any, Any] = load_strategy("data/hard_total.csv")
SOFT_HAND_STRATEGY: dict[Any, Any] = load_strategy("data/soft_total.csv")

def normalize_card(card: object) -> str:
    if isinstance(card, str) and len(card) > 2:
        card = normalize_rank(card)

    if card in {'10', 'J', 'Q', 'K'}:
        return 'KQJ'
    return card

def normalize_rank(card: str) -> str:
    rank = re.sub(r'\W', '', card)
    return rank if rank else card

def hand_value(ranks: list[str]) -> int:
    total: int = 0
    aces: int = ranks.count('A')

    for r in ranks:
        if r in {'K', 'Q', 'J'}:
            total += 10
        elif r != 'A':
            try:
                total += int(r)
            except ValueError:
                print(f"[ERROR] Could not convert rank '{r}' to integer")
                continue

    for _ in range(aces):
        total += 11 if total + 11 <= 21 else 1
    return total

def is_soft_hand(ranks: list[str]) -> bool:
    if 'A' not in ranks:
        return False
    hard_sum: int = hand_value([r for r in ranks if r != 'A'])
    return hard_sum + 11 <= 21

def get_action(player_hand: list[str], dealer_card: str) -> str:
    ranks: list[str] = [normalize_rank(card) for card in player_hand]
    dealer_card = normalize_card(dealer_card)

    if is_soft_hand(ranks):
        non_ace: list[str] = [r for r in ranks if r != 'A']
        if not non_ace:
            key = 'A2'
        else:
            key = 'A' + non_ace[0]
        action = SOFT_HAND_STRATEGY.get(key, {}).get(dealer_card, 'H')
        return action.lower()
    else:
        total = str(hand_value(ranks))
        action = HARD_HAND_STRATEGY.get(total, {}).get(dealer_card, 'H')
        return action.lower()