#!/usr/bin/env python


def main():
    word1 = 'パトカー'
    word2 = 'タクシー'
    zipped = list(zip(word1, word2))
    print(zipped)
    flatten = [char for element in zipped for char in element]
    print(''.join(flatten))


if __name__ == '__main__':
    main()
