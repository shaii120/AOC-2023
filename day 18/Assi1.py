X = 1
Y = 0


def create_table(instructions):
    curr_witdh = 1
    curr_height = 1
    max_width = 1
    min_width = 0
    max_height = 1
    min_height = 0

    for inst in instructions:
        direction, size, color = inst.split(" ")
        size = int(size)
        if direction == "R":
            curr_witdh += size
        elif direction == "D":
            curr_height += size
        elif direction == "L":
            curr_witdh -= size
        elif direction == "U":
            curr_height -= size
        max_height = max(max_height, curr_height)
        min_height = min(min_height, curr_height - 1)
        max_width = max(max_width, curr_witdh)
        min_width = min(min_width, curr_witdh - 1)

    table = [["."] * (max_width - min_width) for _ in range(max_height - min_height)]
    return table, (-min_height, -min_width)


def paint_table_border(table, instructions, starting_location):
    curr_loc = list(starting_location)
    for inst in instructions:
        direction, size, color = inst.split(" ")
        color = "#"  # color[1:-1]
        size = int(size)
        if direction in "R":
            table[curr_loc[Y]][curr_loc[X] : curr_loc[X] + size] = [color] * size
            curr_loc[X] += size
        elif direction in "L":
            table[curr_loc[Y]][curr_loc[X] : curr_loc[X] - size : -1] = [color] * size
            curr_loc[X] -= size
        else:
            step = 1
            if direction == "U":
                step = -1
                size *= -1
            for y in range(curr_loc[Y], curr_loc[Y] + size, step):
                table[y][curr_loc[X]] = color
            curr_loc[Y] += size
    return table


def count_outside_tiles(table):
    outside_check = set()
    total = 0

    for y, line in enumerate(table):
        if line[0] == ".":
            line[0] = "O"
            total += 1
            outside_check.add((y, 1))
        if line[-1] == ".":
            line[-1] = "O"
            total += 1
            outside_check.add((y, len(line) - 2))

    for x in range(len(table[0])):
        if table[0][x] == ".":
            table[0][x] = "O"
            total += 1
            outside_check.add((1, x))
        if table[-1][x] == ".":
            table[-1][x] = "O"
            total += 1
            outside_check.add((len(table) - 2, x))

    while outside_check:
        curr = outside_check.pop()
        if table[curr[Y]][curr[X]] == ".":
            total += 1
            table[curr[Y]][curr[X]] = "O"
            outside_check.add((curr[Y], curr[X] + 1))
            outside_check.add((curr[Y], curr[X] - 1))
            outside_check.add((curr[Y] + 1, curr[X]))
            outside_check.add((curr[Y] - 1, curr[X]))
    return total


def count_painted(instructions):
    table, starting_location = create_table(instructions)
    table = paint_table_border(table, instructions, starting_location)
    outside = count_outside_tiles(table)
    inside = len(table) * len(table[0]) - outside

    return inside


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    print(count_painted(input))


if __name__ == "__main__":
    main()
