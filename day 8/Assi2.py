import re
import functools
import math


# after checking, each starting point walk path exactly 1 ending points following the instructions.
# it'll always be at the end of the instructions.
# after starting at the strating point at following  exactly 1 set of the instruction, you will arrive at a starting point for a loop.
# you'll arrive at the end point at the end of the loop:
# e.g. if you need to follow all the instrucion from the startiong loop position 4 time to close the loop, you will need to follow all of them 3 time time to reach the end point.
# run 'check_loops' on the input to observe.
def find_path_length(instructions, network: dict):
    loops_length = find_loops_lenght(instructions, network)

    return len(instructions) * functools.reduce(
        lambda x, y: int(x * y / math.gcd(x, y)), loops_length
    )  # + 1 - 1


def find_loops_lenght(instructions, network: dict):
    starting_points = [point for point in network.keys() if point[-1] == "A"]
    length_list = []

    for point in starting_points:
        instructions_loops = 0
        postion_at_start = {point: instructions_loops}
        current = point

        while postion_at_start[current] == instructions_loops:
            for inst in instructions:
                if inst == "L":
                    direction = 0
                else:
                    direction = 1

                current = network[current][direction]

            instructions_loops += 1
            if current not in postion_at_start:
                postion_at_start[current] = instructions_loops
            else:
                length_list.append(instructions_loops - postion_at_start[current])
    return length_list


def check_loops(instructions, network: dict):
    starting_points = [point for point in network.keys() if point[-1] == "A"]

    for point in starting_points:
        instructions_loops = 0
        postion_at_start = {point: instructions_loops}
        current = point
        print(f"{point}:")

        while postion_at_start[current] == instructions_loops:
            for idx, inst in enumerate(instructions):
                if inst == "L":
                    direction = 0
                else:
                    direction = 1

                current = network[current][direction]
                if current[-1] == "Z":
                    print(f"\t{current}, {idx + 1}, {instructions_loops}")

            instructions_loops += 1
            if current not in postion_at_start:
                postion_at_start[current] = instructions_loops
            else:
                print(
                    f"{current}, {postion_at_start[current]}, {instructions_loops - postion_at_start[current]}"
                )


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    network = dict()
    pattern = re.compile("\w+")
    instructions = input.pop(0)

    for line in input:
        points = re.findall(pattern, line)
        if len(points) >= 3:
            network[points[0]] = [points[1], points[2]]

    print(find_path_length(instructions, network))


if __name__ == "__main__":
    main()
