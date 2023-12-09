import re
import math


def main():
    with open("input.txt", "r") as file:
        times, distances = file.readlines()
    pattern_num = re.compile(r"\d+")
    times = re.findall(pattern_num, times)
    times = [int(time) for time in times]
    distances = re.findall(pattern_num, distances)
    distances = [int(distance) for distance in distances]
    total = 1

    for time, distance in zip(times, distances):
        min_speed = (time - (time**2 - 4 * distance) ** 0.5) / 2
        min_speed = math.floor(min_speed) + 1
        max_speed = (time + (time**2 - 4 * distance) ** 0.5) / 2
        max_speed = math.ceil(max_speed) - 1
        total *= max_speed - min_speed + 1
        print(max_speed - min_speed)

    print(total)


if __name__ == "__main__":
    main()
