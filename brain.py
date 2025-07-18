import subprocess
import re
from typing import Any

from reader import get_action


# Streak-based betting strategy
class StreakBetting:
    def __init__(self, base_bet=10):
        self.streak = 0
        self.base_bet = base_bet

    def update_result(self, result):
        if result == "win":
            self.streak += 1
        elif result == "lose":
            self.streak = 0

    def get_bet(self, balance):
        bet = self.base_bet + self.streak * 2
        return max(1, min(bet, balance))


def hand_value(ranks: object) -> int | Any:
    total = 0
    ace_count = 0

    for r in ranks:
        if r in ['J', 'Q', 'K']:
            total += 10
        elif r == 'A':
            ace_count += 1
            total += 11
        else:
            try:
                total += int(r)
            except ValueError:
                print(f"[ERROR] Unexpected rank: '{r}'")
                total += 0  # safe fallback

    # Adjust for Aces if total > 21
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total


def parse_hands_from_line(line: object) -> tuple[str, Any] | tuple[str, list[Any]] | tuple[None, None]:
    if line.startswith("Dealer |"):
        # Match all cards after "** " or without it, to get dealer visible cards
        cards = re.findall(r"[♠♦♣♥](\d+|[JQKA])", line)
        if cards:
            dealer_upcard = cards[0]  # only the first visible dealer card
            return "dealer", dealer_upcard
    elif line.startswith("Player |"):
        cards = re.findall(r"[♠♦♣♥](\d+|[JQKA])", line)
        if cards:
            return "player", cards
    return None, None


def read_output(process):
    dealer_hand = None
    player_hand = None

    while True:
        line = process.stdout.readline()
        if not line:
            return "end", None, None  # Process ended

        line = line.strip()
        print(f"[GAME] {line}")  # Show the game output

        if "Current Balance: $" in line:
            match = re.search(r"Current Balance: \$([0-9]+(?:\.[0-9]+)?)", line)
            if match:
                current_balance = float(match.group(1))
                return "balance_update", current_balance, None

        # Parse dealer/player hands as they appear
        role, hand = parse_hands_from_line(line)
        if role == 'dealer':
            dealer_hand = hand
        elif role == 'player':
            player_hand = hand

        # Return game logic
        if "Start a blackjack game?" in line:
            return "start", None, None
        elif "How much would you like to bet" in line:
            return "bet", None, None
        elif "double, hit, or stand" in line:
            # Only proceed if hands are known
            if dealer_hand and player_hand:
                return "decision", dealer_hand, player_hand
            else:
                # If hands are missing, fallback to stand decision
                return "decision", dealer_hand, player_hand
        elif "You win" in line:
            return "result", "win", None
        elif "You busted!" in line or "You lose!" in line:
            return "result", "lose", None
        elif "Push!" in line:
            return "result", "push", None
        elif "See you next time" in line or "You are out of money" in line:
            return "end", None, None


def send_input(process: object, text: object) -> None:
    process.stdin.write(text)
    process.stdin.flush()
    print(f"[BOT] {text.strip()}")


def main():
    game_script = "src/main.py"
    betting = StreakBetting()
    balance = 100
    last_bet = 10

    process = subprocess.Popen(
        ['python3', game_script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    while True:
        state, dealer_hand, player_hand = read_output(process)
        if state == "start":
            send_input(process, "y\n")
        elif state == "bet":
            if balance < 1:
                print(f"[BOT] Balance too low (${balance:.2f}). Exiting.")
                send_input(process, "q\n")
                break
            last_bet = min(betting.get_bet(balance), balance)
            send_input(process, f"{int(last_bet)}\n")
        elif state == "balance_update":
            balance = dealer_hand  # dealer_hand carries the balance value here
        elif state == "decision":
            if dealer_hand and player_hand:
                move = get_action(player_hand, dealer_hand)
                if move not in ['h', 's', 'd']:
                    move = 's'
                send_input(process, move + "\n")
            else:
                send_input(process, "s\n")
        elif state == "result":
            result = dealer_hand  # renamed from dealer_hand to result
            if result == "win":
                balance += last_bet
                betting.update_result("win")
            elif result == "lose":
                balance -= last_bet
                betting.update_result("lose")
            elif result == "push":
                betting.update_result("push")
        elif state == "end":
            print("[BOT] Game ended or exited.")
            break

    process.wait()


if __name__ == "__main__":
    main()
