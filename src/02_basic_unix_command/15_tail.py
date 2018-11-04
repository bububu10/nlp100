#!/usr/bin/env python
import sys


def main():
    args = sys.argv
    n = int(args[1])

    with open('./hightemp.txt') as file:
        max_line = sum([1 for line in file])
        ignore_indexes = list(range(max_line)[:max_line - n])

        # TODO 読み飛ばすループが無駄なので本当は行番号で指定行までseekしたい
        file.seek(0, 0)
        for index, line in enumerate(file):
            if index in ignore_indexes:
                continue
            print(line.rstrip())  # tail -n 10 hightemp.txt


if __name__ == '__main__':
    main()
