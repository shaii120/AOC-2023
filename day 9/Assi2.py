def find_prev_num(num_list: list):
    if len(num_list) == 1:
        return num_list[0]

    delta_list = []

    for i in range(1, len(num_list)):
        delta_list.append(num_list[i] - num_list[i - 1])

    if delta_list == [0] * len(delta_list):
        return num_list[0]
    return num_list[0] - find_prev_num(delta_list)


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    total = 0

    for line in input:
        num_list = line.split(" ")
        num_list = [int(num) for num in num_list]
        total += find_prev_num(num_list)

    print(total)


if __name__ == "__main__":
    main()
