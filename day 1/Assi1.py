import re


def main():
    with open("input.txt", "r") as file:
        input = file.readlines()

    sum = 0
    for line in input:
        digits = re.findall(r"\d", line)
        if digits != []:
            first_digit = digits[0]
            last_digit = digits[-1]
            cal_val = int(first_digit + last_digit)
            sum += cal_val

    print(sum)


if __name__ == "__main__":
    main()
