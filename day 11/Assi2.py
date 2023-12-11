import math

X = 1
Y = 0
EXPANDED_VALUE = 10**6


def find_expanded(universe):
    expanded_list = []
    for idx, line in enumerate(universe):
        if line == ["."] * len(line):
            expanded_list.append(idx)

    return expanded_list


def calc_distance(first, second, expaded_cols, expanded_rows):
    max_col = max(first[X], second[X])
    min_col = min(first[X], second[X])
    max_row = max(first[Y], second[Y])
    min_row = min(first[Y], second[Y])

    row_delta = max_row - min_row
    col_delta = max_col - min_col
    total_expaded = 0

    for col in expaded_cols:
        if min_col < col and col < max_col:
            total_expaded += 1

    for row in expanded_rows:
        if min_row < row and row < max_row:
            total_expaded += 1

    distance = row_delta + col_delta
    distance -= total_expaded
    distance += total_expaded * EXPANDED_VALUE

    return distance


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    universe = [list(line) for line in input]
    expanded_rows = find_expanded(universe)
    # Transpose
    temp = list(map(list, zip(*universe)))
    expaded_cols = find_expanded(temp)

    galaxies_list = []
    total_distances = 0

    for row, line in enumerate(universe):
        for col, tile in enumerate(line):
            if tile == "#":
                galaxies_list.append([row, col])

    for ind, first in enumerate(galaxies_list):
        for second in galaxies_list[ind + 1 :]:
            total_distances += calc_distance(first, second, expaded_cols, expanded_rows)

    print(total_distances)


if __name__ == "__main__":
    main()
