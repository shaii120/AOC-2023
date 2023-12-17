from collections import defaultdict


def hash_word(word):
    val = 0

    for ch in word:
        val += ord(ch)
        val *= 17
        val %= 256

    return val


def remove_word(hashmap: defaultdict, key: str):
    box_num = hash_word(key)
    box: dict = hashmap[box_num]

    if key in box:
        box.pop(key)


def insert_word(hashmap, key, val):
    box_num = hash_word(key)
    box: dict = hashmap[box_num]
    box[key] = int(val)


def get_words_val(words):
    hashmap = defaultdict(lambda: {})
    total = 0

    for word in words:
        if word[-1] == "-":
            remove_word(hashmap, word[:-1])
        else:
            key, val = word.split("=")
            insert_word(hashmap, key, val)

    for box_num, box in hashmap.items():
        for idx, focal_len in enumerate(box.values()):
            curr: int = (box_num + 1) * (idx + 1) * focal_len
            total += curr

    return total


def main():
    with open("input.txt", "r") as file:
        input = file.read().split(",")

    print(get_words_val(input))


if __name__ == "__main__":
    main()
