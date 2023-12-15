import math


def is_mirror_rows(island, place):
    for line in island:
        original = line[:place]
        mirrored = line[place : 2 * place]
        mirrored = mirrored[::-1]
        if original != mirrored:
            return False
    return True


def get_mirror_val(island):
    reverse_island = [line[::-1] for line in island]
    mirror_range = math.ceil(len(island[0]) / 2)

    island_T = list(zip(*island))
    reverse_island_T = [line[::-1] for line in island_T]
    mirror_range_T = math.ceil(len(island_T[0]) / 2)

    for idx in range(1, mirror_range):
        if is_mirror_rows(island, idx):
            return idx
        if is_mirror_rows(reverse_island, idx):
            return len(reverse_island[0]) - idx

    for idx in range(1, mirror_range_T):
        if is_mirror_rows(island_T, idx):
            return 100 * idx
        if is_mirror_rows(reverse_island_T, idx):
            return 100 * (len(reverse_island_T[0]) - idx)

    return 0


def main():
    with open("input.txt", "r") as file:
        input = file.read()
        input = input.split("\n\n")

    sum = 0

    for island in input:
        island = island.splitlines()
        val = get_mirror_val(island)
        sum += val

    print(sum)


if __name__ == "__main__":
    main()
