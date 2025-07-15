import subprocess


def read_output(process):
    while True:
        line = process.stdout.readline()
        if not line:
            return "end"  # Process ended

        line = line.strip()
        print(f"[GAME] {line}")  # Show the game output

        if "Start a blackjack game?" in line:
            return "start"
        elif "How much would you like to bet" in line:
            return "bet"
        elif "double, hit, or stand" in line:
            return "decision"
        elif "See you next time" in line or "You are out of money" in line:
            return "end"


def send_input(process, text):
    process.stdin.write(text)
    process.stdin.flush()
    print(f"[BOT] Sent: {text.strip()}")


def main():
    # Adjust the path to your blackjack game script here:
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
        state = read_output(process)
        if state == "start":
            send_input(process, "y\n")  # Start game automatically
        elif state == "bet":
            send_input(process, "10\n")  # Always bet 10 dollars
        elif state == "decision":
            send_input(process, "h\n")  # Always hit
        elif state == "end":
            print("[BOT] Game ended or exited.")
            break

    process.wait()


if __name__ == "__main__":
    main()