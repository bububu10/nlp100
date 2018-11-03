#!/usr/bin/env python


def main():
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    ignore = str.maketrans({
        ',': '',
        '.': '',
    })
    words = sentence.translate(ignore).split(' ')
    print(words)
    count_list = [len(word) for word in words]
    print(count_list)


if __name__ == '__main__':
    main()
