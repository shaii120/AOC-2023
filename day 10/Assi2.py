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


def find_loop(diagaram: list):
    starting_point = find_starting_point(diagaram)
    prev_point = starting_point
    curr = find_second(diagaram, starting_point)

    rows, cols = len(diagaram), len(diagaram[0])
    loop_diag = [["." for _ in range(cols)] for _ in range(rows)]
    loop_diag[starting_point[Y]][starting_point[X]] = "C"

    while curr != starting_point:
        ch = diagaram[curr[Y]][curr[X]]
        loop_diag[curr[Y]][curr[X]] = ch
        prev_point, curr = curr, find_next(diagaram, curr, prev_point)

    for row, line in enumerate(loop_diag):
        last_c = loop_diag[prev_point[Y]][prev_point[X]]
        for col, tile in enumerate(line):
            if tile == "-":
                loop_diag[row][col] = "P"
            elif (last_c == "L" and tile == "7") or (last_c == "F" and tile == "J"):
                loop_diag[row][col] = "N"
            elif tile != ".":
                loop_diag[row][col] = "C"
                last_c = tile

    return loop_diag


def find_nests_size(diagaram: list):
    loop_diag = find_loop(diagaram)
    size = 0
    for row, line in enumerate(loop_diag):
        is_nest = False
        for col, tile in enumerate(line):
            if tile == "C":
                is_nest = not is_nest
            elif is_nest and tile == ".":
                size += 1
                loop_diag[row][col] = "I"
    return size


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    print(find_nests_size(input))


if __name__ == "__main__":
    main()
