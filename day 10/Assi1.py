import math

X = 1
Y = 0


def find_starting_point(diagaram: list):
    for y, line in enumerate(diagaram):
        x = line.find("S")
        if x != -1:
            return [y, x]


def find_second(diagaram: list, first: list):
    if first[X] > 0:
        point = diagaram[first[Y]][first[X] - 1]
        if point == "-" or point == "F" or point == "L":
            return [first[Y], first[X] - 1]

    if first[Y] > 0:
        point = diagaram[first[Y] - 1][first[X]]
        if point == "|" or point == "F" or point == "7":
            return [first[Y] - 1, first[X]]

    if first[X] < len(diagaram[first[Y]]) - 1:
        point = diagaram[first[Y]][first[X] + 1]
        if point == "-" or point == "7" or point == "J":
            return [first[Y], first[X] + 1]

    if first[Y] < len(diagaram) - 1:
        point = diagaram[first[Y] + 1][first[X]]
        if point == "|" or point == "L" or point == "J":
            return [first[Y] + 1, first[X]]


def find_next(diagaram, curr, prev):
    pipe = diagaram[curr[Y]][curr[X]]

    if pipe == "|":
        if curr[Y] > prev[Y]:
            return [curr[Y] + 1, curr[X]]
        return [curr[Y] - 1, curr[X]]

    if pipe == "-":
        if curr[X] > prev[X]:
            return [curr[Y], curr[X] + 1]
        return [curr[Y], curr[X] - 1]

    if pipe == "L":
        if curr[X] < prev[X]:
            return [curr[Y] - 1, curr[X]]
        return [curr[Y], curr[X] + 1]

    if pipe == "J":
        if curr[X] > prev[X]:
            return [curr[Y] - 1, curr[X]]
        return [curr[Y], curr[X] - 1]

    if pipe == "7":
        if curr[X] > prev[X]:
            return [curr[Y] + 1, curr[X]]
        return [curr[Y], curr[X] - 1]

    if pipe == "F":
        if curr[X] < prev[X]:
            return [curr[Y] + 1, curr[X]]
        return [curr[Y], curr[X] + 1]


def find_loop_length(diagaram: list):
    starting_point = find_starting_point(diagaram)
    prev_point = starting_point
    curr = find_second(diagaram, starting_point)
    loop_length = 0

    while curr != starting_point:
        loop_length += 1
        prev_point, curr = curr, find_next(diagaram, curr, prev_point)

    return loop_length


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    print(math.ceil(find_loop_length(input) / 2))


if __name__ == "__main__":
    main()
