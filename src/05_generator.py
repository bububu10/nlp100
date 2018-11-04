#!/usr/bin/env python
from typing import Sequence, Iterable


def ngram(n: int, seq: Sequence[str]) -> Iterable[str]:
    rest = seq
    while len(rest) is not n - 1:
        yield rest[0:n]
        rest = rest[n - 1:]


def main():
    sentence = 'I am an NLPer'
    words = sentence.split(' ')

    print(list(ngram(2, sentence)))
    print(list(ngram(2, words)))


if __name__ == '__main__':
    main()
