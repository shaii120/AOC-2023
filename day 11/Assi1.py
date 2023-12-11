import math

X = 1
Y = 0


def expand(universe):
    expanded_universe = []
    for line in universe:
        expanded_universe.append(line)
        if line == ["."] * len(line):
            expanded_universe.append("." * len(line))

    return expanded_universe


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    input = [list(line) for line in input]
    new_universe = expand(input)
    # Transpose
    temp = list(map(list, zip(*new_universe)))
    temp = expand(temp)
    new_universe = list(map(list, zip(*temp)))

    galaxies_list = []
    total_distances = 0

    for row, line in enumerate(new_universe):
        for col, tile in enumerate(line):
            if tile == "#":
                galaxies_list.append([row, col])

    for ind, first in enumerate(galaxies_list):
        for second in galaxies_list[ind + 1 :]:
            distance = abs(first[X] - second[X]) + abs(first[Y] - second[Y])
            total_distances += distance

    print(total_distances)


if __name__ == "__main__":
    main()
