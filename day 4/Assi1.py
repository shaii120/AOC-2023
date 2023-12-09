import re


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    pattern_num = re.compile(r"\d+")
    sum = 0

    for line in input:
        points = 0.5
        temp = line.split(": ")[1]
        win_nums, guesses = temp.split(" | ")
        win_nums = re.findall(pattern_num, win_nums)
        guesses = re.findall(pattern_num, guesses)
        for guess in guesses:
            if guess in win_nums:
                points *= 2
        sum += int(points)
    print(sum)


if __name__ == "__main__":
    main()
