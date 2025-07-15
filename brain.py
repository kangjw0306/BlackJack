import subprocess
import re
from reader import get_action


def hand_value(ranks):
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


def parse_hands_from_line(line):
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
        elif "See you next time" in line or "You are out of money" in line:
            return "end", None, None


def send_input(process, text):
    process.stdin.write(text)
    process.stdin.flush()
    print(f"[BOT] {text.strip()}")


def main():
    game_script = "src/main.py"

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
            send_input(process, "y\n")  # Start game automatically
        elif state == "bet":
            send_input(process, "10\n")  # Always bet 10 dollars
        elif state == "decision":
            if dealer_hand and player_hand:
                # Get bot move based on strategy from reader.py
                move = get_action(player_hand, dealer_hand)
                if move not in ['h', 's', 'd']:
                    move = 's'  # fallback to stand if invalid
                send_input(process, move + "\n")
            else:
                # Missing hand info, default to stand
                send_input(process, "s\n")
        elif state == "end":
            print("[BOT] Game ended or exited.")
            break

    process.wait()


if __name__ == "__main__":
    main()