def calc_val(idx, amount):
    stop_val = idx + 2
    start_val = stop_val - amount
    return sum(range(start_val, stop_val))


def get_col_val(col):
    rocks_between_cubes = 0
    col_val = 0

    for idx, tile in enumerate(reversed(col)):
        if tile == "O":
            rocks_between_cubes += 1
        elif tile == "#":
            col_val += calc_val(idx - 1, rocks_between_cubes)
            rocks_between_cubes = 0
    col_val += calc_val(idx, rocks_between_cubes)

    return col_val


def get_table_val(table):
    table_T = list(zip(*table))
    total = 0

    for col in table_T:
        total += get_col_val(col)

    return total


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    print(get_table_val(input))


if __name__ == "__main__":
    main()
