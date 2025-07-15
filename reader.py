import csv

def load_strategy(filename):
    strategy = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)[1:]

        for row in reader:
            player_sum = int(row[0])
            strategy[player_sum] = dict(zip(headers, row[1:]))

        return strategy

def normalize_dealer_card(card):
    if card in {'10', 'J', 'Q', 'K'}:
        return 'KQJ'
    return card

def get_action(strategy, player_sum, dealer_card):
    dealer_card = normalize_dealer_card(str(dealer_card))
    return strategy.get(player_sum, {}).get(dealer_card, 'H')



print(load_strategy('data/hard_total.csv'))

strat = load_strategy('data/hard_total.csv')
action = get_action(strat, player_sum=12, dealer_card='4')
print(action)  # → 'S'