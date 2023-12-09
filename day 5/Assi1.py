import re


class range_dict:
    def __init__(self) -> None:
        self.dr = dict()

    def add(self, dst, src, rng):
        self.dr[range(src, src + rng)] = dst

    def get(self, src):
        for key in self.dr:
            if src in key:
                return self.dr[key] + (src - key.start)
        return src


def main():
    with open("input.txt", "r") as file:
        seeds, input = file.read().split("\n", 1)
    pattern_num = re.compile(r"\d+")
    pattern_map_line = re.compile(r"[\d| ]+")
    input = re.finditer(r"([\d| ]+\n)+", input)
    src = re.findall(pattern_num, seeds)
    src = [int(val) for val in src]

    for mapping in input:
        mapped = range_dict()
        map_lines = re.findall(pattern_map_line, mapping.group())
        for line in map_lines:
            line = line.split(" ")
            line = [int(val) for val in line]
            mapped.add(*line)
        src = [mapped.get(val) for val in src]

    print(min(src))


if __name__ == "__main__":
    main()
