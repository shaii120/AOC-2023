RIGHT = 0  # 00
UP = 1  # 01
LEFT = 2  # 10
DOWN = 3  # 11

X = 1
Y = 0


class beam_calculator:
    def __init__(self, table, init_loc=(0, 0), init_dir=RIGHT) -> None:
        self.table = table
        initial_beam = (init_loc, init_dir)
        self.curr_beams = [initial_beam]
        self.all_beams = []

    def in_boundry(self, location):
        return 0 <= location[X] < len(self.table[0]) and (
            0 <= location[Y] < len(self.table)
        )

    def handle_direction(self, tile, direction, location):
        new_direction = direction
        beam = (location, direction)

        if tile == "|" and direction in (RIGHT, LEFT):
            new_direction = DOWN
            new_beam = (location, UP)
            if new_beam not in self.all_beams:
                self.curr_beams.append(new_beam)
                self.all_beams.append(beam)
        elif tile == "-" and direction in (UP, DOWN):
            new_direction = RIGHT
            new_beam = (location, LEFT)
            if new_beam not in self.all_beams:
                self.curr_beams.append(new_beam)
                self.all_beams.append(beam)
        elif tile == "\\":
            new_direction ^= 3  # 11
            self.all_beams.append(beam)
        elif tile == "/":
            new_direction ^= 1  # 01
            self.all_beams.append(beam)

        return new_direction

    def handle_location(self, location, direction):
        if direction == RIGHT:
            return location[Y], location[X] + 1
        if direction == UP:
            return location[Y] - 1, location[X]
        if direction == LEFT:
            return location[Y], location[X] - 1
        # DOWN
        return location[Y] + 1, location[X]

    def count_energized(self):
        energized = set()

        while self.curr_beams != []:
            location, direction = self.curr_beams.pop()
            while (
                self.in_boundry(location)
                and (location, direction) not in self.all_beams
            ):
                energized.add(location)
                tile = self.table[location[Y]][location[X]]
                direction = self.handle_direction(tile, direction, location)
                location = self.handle_location(location, direction)

        return len(energized)


def max_beam(table):
    max_energized = 0
    table_y_len = len(table) - 1
    table_x_len = len(table[0]) - 1

    for y in range(len(table)):
        left = beam_calculator(table, (y, 0), RIGHT).count_energized()
        right = beam_calculator(table, (y, table_x_len), LEFT).count_energized()
        max_energized = max(max_energized, left, right)

    for x in range(len(table[0])):
        top = beam_calculator(table, (0, x), DOWN).count_energized()
        bottom = beam_calculator(table, (table_y_len, x), UP).count_energized()
        max_energized = max(max_energized, top, bottom)

    return max_energized


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    print(max_beam(input))


if __name__ == "__main__":
    main()
