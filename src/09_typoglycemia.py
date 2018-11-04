#!/usr/bin/env python
from random import sample


def shuffle(word: str) -> str:
    middle = word[1:-1]
    return word[0] + "".join(sample(middle, len(middle))) + word[-1]


def main():
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = sentence.split(' ')
    print(words)

    shuffled = [shuffle(word) if (len(word) > 4) else word for word in words]
    print(" ".join(shuffled))


if __name__ == '__main__':
    main()
