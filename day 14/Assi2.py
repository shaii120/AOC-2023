import re


def calc_between_cubes(idx, last_cube, rocks_between_cubes):
    total = idx - last_cube - 1
    dot_amount = total - rocks_between_cubes
    new_row = ""
    new_row += "O" * rocks_between_cubes
    new_row += "." * dot_amount

    return new_row


def tilt_row_left(row):
    rocks_between_cubes = 0
    new_row = ""
    last_cube = -1

    for idx, tile in enumerate(row):
        if tile == "O":
            rocks_between_cubes += 1
        elif tile == "#":
            new_row += calc_between_cubes(idx, last_cube, rocks_between_cubes)
            new_row += "#"
            rocks_between_cubes = 0
            last_cube = idx
    new_row += calc_between_cubes(idx + 1, last_cube, rocks_between_cubes)

    return new_row


def tilt_table_up(table):
    table_T = zip(*table)
    new_table_T = tilt_table_left(table_T)
    new_table = tuple(zip(*new_table_T))

    return new_table


def tilt_table_left(table):
    new_table = [tilt_row_left(row) for row in table]
    return new_table


def tilt_table_down(table):
    table_reversed = reversed(table)
    new_table_reversed = tilt_table_up(table_reversed)
    new_table = tuple(reversed(new_table_reversed))

    return new_table


def tilt_table_right(table):
    table_T = list(zip(*table))
    new_table_T = tilt_table_down(table_T)
    new_table = tuple(zip(*new_table_T))

    return new_table


def tilt_one_cicle(table):
    table = tilt_table_up(table)
    table = tilt_table_left(table)
    table = tilt_table_down(table)
    return tilt_table_right(table)


def find_loop(table, max_tries):
    table = tuple(table)
    table_hash = {table: 0}

    for idx in range(max_tries):
        table = tilt_one_cicle(table)
        if table in table_hash:
            return (idx + 1), table, idx - table_hash[table]
        table_hash[table] = idx

    return idx, table, max_tries


def tilt_all_circles(table, amount):
    table = tuple(table)
    itr_num, table, loop_len = find_loop(table, amount)

    amount -= itr_num
    amount %= loop_len
    print(itr_num, loop_len, amount)

    for _ in range(amount):
        table = tilt_one_cicle(table)
    return table


def calc_val(table):
    total = 0
    pattern = re.compile("O")
    for idx, row in enumerate(reversed(table)):
        row = "".join(row)
        cubes = re.findall(pattern, row)
        total += len(cubes) * (idx + 1)

    return total


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    tilts_circles = 1000000000
    input = tilt_all_circles(input, tilts_circles)

    print(calc_val(input))


if __name__ == "__main__":
    main()
