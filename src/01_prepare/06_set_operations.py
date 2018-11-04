#!/usr/bin/env python
from typing import Sequence, Iterable


def ngram(n: int, seq: Sequence[str]) -> Iterable[str]:
    rest = seq
    while len(rest) is not n - 1:
        yield rest[0:n]
        rest = rest[n - 1:]


def main():
    word1 = 'paraparaparadise'
    word2 = 'paragraph'

    x = set(ngram(2, word1))
    y = set(ngram(2, word2))

    print('x: ' + str(x))
    print('y: ' + str(y))

    print('x | y: ' + str(x | y))
    print('x & y: ' + str(x & y))
    print('x - y: ' + str(x - y))

    print('x contains "se": ' + str('se' in x))
    print('y contains "se": ' + str('se' in y))


if __name__ == '__main__':
    main()
