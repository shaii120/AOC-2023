import re
import functools


class range_dict:
    def __init__(self) -> None:
        self.dr = dict()

    def add(self, dst, src, rng):
        self.dr[range(src, src + rng)] = dst

    def get(self, src):
        for key in self.dr:
            if src in key:
                return src + (self.dr[key] - key.start)
        return src

    def get_ranges(self, src: range):
        dst_ranges = []
        src_list = [src]

        for key in self.dr:
            new_src_list = []
            for val in src_list:
                if overlaps(src, key):
                    start = max(val.start, key.start)
                    end = min(val.stop, key.stop)

                    if val.start < start:
                        new_src_list.append(range(val.start, start))
                    if end < val.stop:
                        new_src_list.append(range(end, val.stop))

                    dst = range(start, end)
                    delta = self.dr[key] - key.start
                    dst = range(dst.start + delta, dst.stop + delta)
                    dst_ranges.append(dst)
                else:
                    new_src_list.append(val)
            src_list = new_src_list

        if src_list != []:
            dst_ranges += src_list

        return dst_ranges


def overlaps(x: range, y: range):
    return max(x.start, y.start) < min(x.stop, y.stop)


def main():
    with open("input.txt", "r") as file:
        seeds, input = file.read().split("\n", 1)
    pattern_num_pair = re.compile(r"\d+ \d+")
    pattern_map_line = re.compile(r"[\d| ]+")
    input = re.finditer(r"([\d| ]+\n)+", input)
    seeds = re.findall(pattern_num_pair, seeds)
    src = []

    for val in seeds:
        start, rng = val.split(" ")
        start = int(start)
        rng = int(rng)
        src.append(range(start, start + rng))

    print(src)
    for mapping in input:
        mapped = range_dict()
        map_lines = re.findall(pattern_map_line, mapping.group())
        for line in map_lines:
            line = line.split(" ")
            line = [int(val) for val in line]
            mapped.add(*line)
        src = functools.reduce(lambda acc, cur: acc + mapped.get_ranges(cur), src, [])
    print(min([val.start for val in src]))


if __name__ == "__main__":
    main()
