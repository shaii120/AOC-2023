import re
import math


def main():
    with open("input.txt", "r") as file:
        time, distance = file.readlines()
    pattern_num = re.compile(r"\d+")
    time = re.findall(pattern_num, time)
    time = int("".join(time))
    distance = re.findall(pattern_num, distance)
    distance = int("".join(distance))
    total = 1

    min_speed = (time - (time**2 - 4 * distance) ** 0.5) / 2
    min_speed = math.floor(min_speed) + 1
    max_speed = (time + (time**2 - 4 * distance) ** 0.5) / 2
    max_speed = math.ceil(max_speed) - 1
    total *= max_speed - min_speed + 1

    print(total)


if __name__ == "__main__":
    main()
