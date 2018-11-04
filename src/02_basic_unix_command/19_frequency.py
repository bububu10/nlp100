#!/usr/bin/env python
from collections import Counter


def main():
    with open('./hightemp.txt') as file:
        first_cols = list(line.split()[0] for line in file.readlines())
        counter = Counter(first_cols)
        print(counter)
        for word in counter.most_common():
            print(word[0])  # sort -k 1 -t $'\t' hightemp.txt | cut -f 1 | uniq -c | sort -r


if __name__ == '__main__':
    main()
