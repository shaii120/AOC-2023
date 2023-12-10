import re


def find_path(instructions, network):
    current = "AAA"
    TARGET = "ZZZ"
    steps = 0
    while True:
        for inst in instructions:
            steps += 1
            if inst == "L":
                current = network[current][0]
            else:
                current = network[current][1]

            if current == TARGET:
                return steps


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

    print(find_path(instructions, network))


if __name__ == "__main__":
    main()
