import re


def find_row_adjacent(col, numbers):
    adjacent_numbers = []
    for num in numbers:
        num_range = num.span()
        if num_range[0] <= col + 1 and col <= num_range[1]:
            adjacent_numbers.append(int(num.group()))
    return adjacent_numbers


def find_ratio(row, col, numbers, text):
    adjacent_nums = []
    if row > 0:
        adjacent_nums += find_row_adjacent(col, numbers[row - 1])
    if row < len(text) - 1:
        adjacent_nums += find_row_adjacent(col, numbers[row + 1])
    adjacent_nums += find_row_adjacent(col, numbers[row])

    if len(adjacent_nums) == 2:
        return adjacent_nums[0] * adjacent_nums[1]
    return 0


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    pattern_num = re.compile(r"\d+")
    pattern_ratio = re.compile(r"\*")
    numbers = []
    sum = 0

    for line in input:
        nums_iter = re.finditer(pattern_num, line)
        numbers.append([num for num in nums_iter])

    for row, line in enumerate(input):
        ratios = re.finditer(pattern_ratio, line)
        for ratio in ratios:
            num = find_ratio(row, ratio.span()[0], numbers, input)
            sum += int(num)
    print(sum)


if __name__ == "__main__":
    main()
