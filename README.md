# BlackJack CLI

A simple command-line blackjack bot made with Python. Features both an interactive game and an automated bot that follows basic strategy.

## Features

### Current Features
- **Two-deck shoe**: Uses a standard two-deck setup
- **Standard blackjack rules**: Ace + 10-value card = blackjack
- **Player options**: Hit, Stand, Double Down
- **Dealer behavior**: Stands on soft 17, follows house rules
- **Automated bot**: Plays using basic strategy without card counting
- **Interactive gameplay**: Manual play mode for human players

### Planned Features
- Card splitting functionality
- Insurance and side bets
- Surrender option
- Advanced bot strategies with card counting

## Game Rules

### Initial Deal
- Player and dealer each receive 2 cards
- Dealer's first card is hidden (shows as `**`)
- Dealer's second card is visible

### Player Options
- **Hit**: Take another card
- **Stand**: Keep current hand
- **Double Down**: Double the bet and take exactly one more card

### Dealer Rules
- Dealer stands on soft 17
- Dealer must hit on 16 or below
- Dealer reveals hidden card after player's turn

### Winning Conditions
- **Blackjack**: Ace + 10-value card (pays 3:2)
- **Standard win**: Hand closer to 21 than dealer without busting
- **Push**: Tie with dealer
- **Bust**: Hand exceeds 21 (automatic loss)

## Installation

### Prerequisites
- Python 3.8 or higher
- No external dependencies required (uses only standard library)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/kangjw0306/BlackJack.git
   cd BlackJack
   ```

2. No additional setup required - the project uses only Python standard library modules.

## Usage

### Running the Bot
To run the automated blackjack bot:
```bash
python3 brain.py
```

The bot will:
- Play automatically using basic strategy
- Continue until balance reaches $0
- Follow optimal blackjack decisions without card counting

### Playing the Game Manually
To play blackjack interactively:
```bash
python3 src/main.py
```

This launches the interactive game where you can:
- Make your own decisions (hit, stand, double down)
- Control betting amounts
- Play at your own pace

## Project Structure

```
BlackJack/
├── bot/
│   ├── brain.py          # Automated bot implementation
│   └── reader.py         # Strategy parsing and hand analysis
├── src/
│   └── main.py           # Interactive game implementation
├── config.toml           # Game configuration settings
├── pyproject.toml        # Python project configuration
└── README.md             # This file
```

## Configuration

The game can be configured using the `config.toml` file. Key settings include:

- **Deck settings**: Number of decks, shuffle timing

## Development

### Architecture
- **brain.py**: Contains the bot logic and basic strategy implementation
- **src/main.py**: Interactive game engine with user input handling
- **Standard library only**: No external dependencies for easy deployment

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Planned Improvements
- [ ] Card splitting functionality
- [ ] Insurance bets
- [ ] Surrender option
- [ ] Advanced card counting strategies
- [ ] Statistical analysis and reporting

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.

For more details, see the [Creative Commons BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/).

## Author

**Jiwon Kang**
- Email: kangjw0306@gmail.com
- GitHub: [@kangjw0306](https://github.com/kangjw0306)
