def hash_word(word):
    val = 0

    for ch in word:
        val += ord(ch)
        val *= 17
        val %= 256

    return val


def get_words_val(words):
    total = 0

    for word in words:
        total += hash_word(word)

    return total


def main():
    with open("input.txt", "r") as file:
        input = file.read().split(",")

    print(get_words_val(input))


if __name__ == "__main__":
    main()
