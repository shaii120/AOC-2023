import regex as re


def main():
    with open("input.txt", "r") as file:
        input = file.readlines()

    sum = 0
    written_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    replacement_pattern = "|".join(written_digits.keys())
    pattern = re.compile(f"\\d|{replacement_pattern}")
    
    for line in input:
        digits = re.findall(pattern, line, overlapped=True)
        if digits != []:
            first_digit = digits[0]
            last_digit = digits[-1]
            if first_digit in written_digits:
                first_digit = written_digits[first_digit]
            if last_digit in written_digits:
                last_digit = written_digits[last_digit]

            cal_val = int(first_digit + last_digit)
            sum += cal_val

    print(sum)


if __name__ == "__main__":
    main()
