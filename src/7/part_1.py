def is_five_of_kind(cards: dict) -> bool:
    return len(cards) == 1

def is_four_of_kind(cards: dict) -> bool:
    if len(cards) == 2:
        keys = cards.keys()
        return cards[keys[0]] == 4 or cards[keys[1]] == 4
    return False

def is_full_house(cards: dict) -> bool:
    if len(cards) == 2:
        keys = cards.keys()
        return cards[keys[0]] == 3 or cards[keys[1]] == 3
    return False

def is_three_of_kind(cards: dict) -> bool:
    if len(cards) == 3:
        keys = cards.keys()
        return cards[keys[0]] == 3 or cards[keys[1]] == 3 or cards[keys[2]] == 3
    return False

def is_two_pair(cards: dict) -> bool:
    if len(cards) == 3:
        keys = cards.keys()
        return cards[keys[0]] == 2 or cards[keys[1]] == 2 or cards[keys[2]] == 2
    return False

def is_one_pair(cards: dict) -> bool:
    if len(cards) == 4:
        keys = cards.keys()
        return cards[keys[0]] == 2 or cards[keys[1]] == 2 or cards[keys[2]] == 2 or cards[keys[3]] == 2
    return False

def is_high_card(cards: dict) -> bool:
    return len(cards) == 5


def compare(line1: str, line2: str) -> bool:
    _, hand1 = line1.split(' ')
    cards1 = {}
    for card in hand1:
        if card not in cards1:
            cards1[card] = 0
        cards1[card] += 1
    
    _, hand2 = line2.split(' ')
    cards2 = {}
    for card in hand2:
        if card not in cards2:
            cards2[card] = 0
        cards2[card] += 1

    # TODO: compare hands


with open('src/7/test.txt', 'r') as fp:
    lines = fp.readlines()
