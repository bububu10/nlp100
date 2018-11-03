#!/usr/bin/env python


def main():
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    ignore = str.maketrans({
        ',': '',
        '.': '',
    })

    words = sentence.translate(ignore).split(' ')
    print(words)

    pickups = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    pickup_indexes = [index - 1 for index in pickups]
    print(pickup_indexes)

    chars = [word[0] if (index in pickup_indexes) else word[0:2] for index, word in enumerate(words)]
    print(chars)


if __name__ == '__main__':
    main()
