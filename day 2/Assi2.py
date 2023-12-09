import re
import functools


def game_check_minimum(stages: str):
    game_stages = stages.split("; ")
    colors = {"red": 0, "green": 0, "blue": 0}

    for stage in game_stages:
        result = stage.split(", ")
        for pair in result:
            num, color = pair.split(" ")
            num = int(num)
            colors[color] = max(num, colors[color])
    return functools.reduce(lambda x, y: x * y, colors.values())


def main():
    with open("input.txt", "r") as file:
        input = file.readlines()

    id_pattern = re.compile(r" (\d*):")

    sum = 0

    for game in input:
        # remove '\n'
        game = game[:-1]
        id = re.findall(id_pattern, game)[0]
        id = int(id)
        game_stages = game.split(": ")[1]

        sum += game_check_minimum(game_stages)

    print(sum)


if __name__ == "__main__":
    main()
