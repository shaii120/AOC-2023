import re
from collections import defaultdict

CARD_BASE = 16


def card_value(card):
    special_cards_val = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    if card in special_cards_val:
        return special_cards_val[card]
    return int(card)


def hand_might(hand: str):
    cards = defaultdict(lambda: 0)
    series = defaultdict(lambda: [])
    # Reversing the string so the last card will be the least significant
    hand = hand[::-1]

    secondary_power = 0
    for card in hand:
        cards[card] += 1
        secondary_power += card_value(card)
        secondary_power /= CARD_BASE

    for card, amount in cards.items():
        series[amount] += [card_value(card)]
        series[amount].sort(reverse=True)

    if 5 in series:
        return 6 + secondary_power
    if 4 in series:
        return 5 + secondary_power
    if 3 in series:
        if 2 in series:
            return 4 + secondary_power
        return 3 + secondary_power
    if 2 in series:
        if len(series[2]) == 2:
            return 2 + secondary_power
        return 1 + secondary_power
    return secondary_power


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    hands = dict()
    total = 0

    for line in input:
        hand, bid = line.split(" ")
        hands[hand_might(hand)] = int(bid)

    for idx, key in enumerate(sorted(hands)):
        rank = idx + 1
        total += rank * hands[key]

    print(total)


if __name__ == "__main__":
    main()
