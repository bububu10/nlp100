#!/usr/bin/env python
import sys


def main():
    args = sys.argv
    n = int(args[1])

    with open('./hightemp.txt') as file:
        for index, line in enumerate(file):
            if index is n:
                return
            print(line.replace('\n', ''))  # head -n 10 hightemp.txt


if __name__ == '__main__':
    main()
