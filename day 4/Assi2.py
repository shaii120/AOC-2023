import re
import functools


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    pattern_num = re.compile(r"\d+")
    scratch_cards = [1] * len(input)

    for id, line in enumerate(input):
        wins = 0
        temp = line.split(": ")[1]
        win_nums, guesses = temp.split(" | ")
        win_nums = re.findall(pattern_num, win_nums)
        guesses = re.findall(pattern_num, guesses)
        for guess in guesses:
            if guess in win_nums:
                wins += 1
        for i in range(1, wins + 1):
            if id + i < len(input):
                scratch_cards[id + i] += scratch_cards[id]
    print(scratch_cards)
    sum = functools.reduce(lambda x, y: x + y, scratch_cards)
    print(sum)


if __name__ == "__main__":
    main()
