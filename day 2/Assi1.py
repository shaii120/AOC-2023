import re
from collections import defaultdict


def game_check(stages: str, condition: dict):
    game_stages = stages.split("; ")

    for stage in game_stages:
        result = stage.split(", ")
        for pair in result:
            num, color = pair.split(" ")
            num = int(num)
            if num > condition[color]:
                return False
    return True


def main():
    with open("input.txt", "r") as file:
        input = file.readlines()

    id_pattern = re.compile(r" (\d*):")
    game_condition = {"red": 12, "green": 13, "blue": 14}

    sum = 0

    for game in input:
        # remove '\n'
        game = game[:-1]
        id = re.findall(id_pattern, game)[0]
        id = int(id)
        game_stages = game.split(": ")[1]

        if game_check(game_stages, game_condition):
            sum += id

    print(sum)


if __name__ == "__main__":
    main()
