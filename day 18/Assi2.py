X = 0
Y = 1


def get_new_instruction(color):
    size = color[2:7]
    size = int(size, 16)
    direction = color[7]

    if direction == "0":
        direction = "R"
    elif direction == "1":
        direction = "D"
    elif direction == "2":
        direction = "L"
    else:  # == "3"
        direction = "U"

    return size, direction


def calc_polygon_points(instructions):
    curr_X, curr_Y = 0, 0
    points = []
    perimeter = 0

    for inst in instructions:
        direction, size, color = inst.split(" ")
        # size = int(size)
        size, direction = get_new_instruction(color)
        perimeter += size

        if direction == "R":
            curr_X += size
        elif direction == "L":
            curr_X -= size
        elif direction == "D":
            curr_Y += size
        else:  # direction == "U"
            curr_Y -= size
        points.append((curr_X, curr_Y))

    return points, perimeter


def calc_polygon_area(points):
    print(points)
    area = points[-1][X] * points[0][Y] - points[0][X] * points[-1][Y]

    for idx in range(len(points) - 1):
        area += points[idx][X] * points[idx + 1][Y]
        area -= points[idx + 1][X] * points[idx][Y]
    area /= 2

    return abs(area)


def count_painted(instructions):
    points, perimeter = calc_polygon_points(instructions)
    shape = calc_polygon_area(points)
    lagoon_area = shape + perimeter / 2 + 1

    return lagoon_area


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    print(count_painted(input))


if __name__ == "__main__":
    main()
