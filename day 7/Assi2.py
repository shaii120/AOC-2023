import re
from collections import defaultdict

CARD_BASE = 16


def card_value(card):
    special_cards_val = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    if card in special_cards_val:
        return special_cards_val[card]
    return int(card)


def hand_might(hand: str):
    cards = defaultdict(lambda: 0)
    series = defaultdict(lambda: 0)
    # Reversing the string so the last card will be the least significant
    hand = hand[::-1]

    sorted

    secondary_power = 0
    max_not_jocker = 0

    for card in hand:
        cards[card] += 1
        secondary_power += card_value(card)
        secondary_power /= CARD_BASE

    for card, amount in cards.items():
        if card != "J" and amount > max_not_jocker:
            max_not_jocker = amount
        series[amount] += 1

    if max_not_jocker != 0 and cards["J"] != 0:
        jocker_amount = cards["J"]
        series[max_not_jocker] -= 1
        series[jocker_amount] -= 1
        series[max_not_jocker + jocker_amount] += 1

    if 5 in series:
        return 6 + secondary_power
    if 4 in series:
        return 5 + secondary_power
    if 3 in series:
        if series[2] > 0:
            return 4 + secondary_power
        return 3 + secondary_power
    if 2 in series:
        if series[2] == 2:
            return 2 + secondary_power
        return 1 + secondary_power
    return secondary_power


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    hands = dict()
    debug = dict()
    total = 0

    for line in input:
        hand, bid = line.split(" ")
        hands[hand_might(hand)] = int(bid)
        debug[hand_might(hand)] = hand

    for idx, key in enumerate(sorted(hands)):
        rank = idx + 1
        print(f"{debug[key]}, {key}, {hands[key]}")
        total += rank * hands[key]

    print(total)


if __name__ == "__main__":
    main()
