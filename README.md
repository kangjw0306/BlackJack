# Blackjack

A simple CLI blackjack bot made with Python.

Currently, supports hitting, standing, and doubling.  
Splitting is being worked on.  

---

## Game Rules:

1. **Deck**: Two-deck shoe  
2. **Initial Deal**:  
   - Player and dealer each get 2 cards  
   - Dealer hides the first card (`**`) and shows the second  
   - No side bets or insurance (yet...)  
3. **Blackjack Definition**:  
   - Ace + 10-value card  
4. **Player Options**:  
   - Hit, Stand, Double Down  
   - No splitting or surrender (yet...)  
5. **Dealer Behavior**:  
   - Stands on soft 17  

---

## Bot Rules

1. Plays until balance is $0
2. Follows baisic strategy without card counting

---

## To Run

To run the bot, download all included files and run:

```bash
python3 brain.py
```

To run the blackjack game itself, run:
```bash
python3 src/main.py
```
