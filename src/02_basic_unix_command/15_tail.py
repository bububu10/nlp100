#!/usr/bin/env python
import sys


def main():
    args = sys.argv
    n = int(args[1])

    with open('./hightemp.txt') as file:
        max_line = sum([1 for line in file])
        ignore_indexes = list(range(max_line)[:max_line - n])
        file.seek(0, 0)
        for index, line in enumerate(file):
            if index in ignore_indexes:
                continue
            print(line.rstrip())


if __name__ == '__main__':
    main()
