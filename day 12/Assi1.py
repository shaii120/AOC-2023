import re
from functools import lru_cache
import copy


pattern_dot = re.compile(r"\.+")
pattern_spring = re.compile(r"#+")


@lru_cache(maxsize=None)
def calc_arragements(record: str, spring_pattern: tuple, streak: bool):
    if spring_pattern == ():
        if record.find("#") == -1:
            return 1
        return 0
    elif spring_pattern[0] == 0:
        return calc_arragements(record[1:], spring_pattern[1:], False)
    elif spring_pattern[0] < 0 or record == "":
        return 0

    curr_char = record[0]

    if curr_char == ".":
        if streak:
            return 0

        dots = re.search(pattern_dot, record)
        length = len(dots.group())
        return calc_arragements(record[length:], spring_pattern, False)

    if curr_char == "#":
        springs = re.search(pattern_spring, record)
        length = len(springs.group())
        new_spring_pattern = list(copy.copy(spring_pattern))
        new_spring_pattern[0] -= length
        new_spring_pattern = tuple(new_spring_pattern)
        return calc_arragements(record[length:], new_spring_pattern, True)

    # elif curr_char == "?":
    skip = 1
    new_spring_pattern = list(copy.copy(spring_pattern))
    new_spring_pattern[0] -= 1
    if len(record) > 1 and record[1] == "#":
        springs = re.search(pattern_spring, record[1:])
        length = len(springs.group())
        new_spring_pattern[0] -= length
        skip += length
    new_spring_pattern = tuple(new_spring_pattern)
    arragements = calc_arragements(record[skip:], new_spring_pattern, True)
    if not streak:
        arragements += calc_arragements(record[1:], spring_pattern, False)
    return arragements


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    total_arrangements = 0

    for line in input:
        record, spring_pattern = line.split(" ")
        record = "?".join([record] * 5)
        spring_pattern = ",".join([spring_pattern] * 5)
        spring_pattern = [int(val) for val in spring_pattern.split(",")]
        spring_pattern = tuple(spring_pattern)
        arrangements = calc_arragements(record, spring_pattern, False)
        total_arrangements += arrangements
        # print(f"{arrangements}: {record} {spring_pattern}")

    print(total_arrangements)


if __name__ == "__main__":
    main()
