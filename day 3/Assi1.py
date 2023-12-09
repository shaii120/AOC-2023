import re


def above_below(row, col, default_chars, text):
    if row > 0 and text[row - 1][col] not in default_chars:
        return True
    if row < len(text) - 1 and text[row + 1][col] not in default_chars:
        return True


def find_sign(row, col_index, text):
    def_chars = "1234567890."
    if col_index[0] > 0:
        col = col_index[0] - 1
        if above_below(row, col, def_chars, text) or text[row][col] not in def_chars:
            return True

    if col_index[1] < len(text[row]):
        col = col_index[1]
        if above_below(row, col, def_chars, text) or text[row][col] not in def_chars:
            return True

    for col in range(*col_index):
        if above_below(row, col, def_chars, text):
            return True

    return False


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    pattern = re.compile(r"\d+")
    sum = 0

    for row, line in enumerate(input):
        nums = re.finditer(pattern, line)
        for num in nums:
            if find_sign(row, num.span(), input):
                num = int(num.group())
                sum += int(num)

    print(sum)


if __name__ == "__main__":
    main()
