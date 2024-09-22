def split_deck(cards: list):
    cutsize = int(len(cards)/2)
    split1 = cards[:cutsize]
    split2 = cards[cutsize:]
    return split1, split2

def cut(cards: list):
    split1, split2 = split_deck(cards)
    return [*split2, *split1]

def shuffle(cards):
    deck = []
    split1, split2 = split_deck(cards)
    for card1, card2 in zip(split1, split2):
        deck.append(card1)
        deck.append(card2)
    return deck

cards = input().split()
operations = input()
for operation in operations:
    if operation == "C":
        cards = cut(cards)
    elif operation == "S":
        cards = shuffle(cards)
print(*cards)