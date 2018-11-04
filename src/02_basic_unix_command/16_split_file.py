#!/usr/bin/env python
import math
import sys


def main():
    args = sys.argv
    n = int(args[1])

    file = open('./hightemp.txt')
    line_count = sum([1 for line in file])
    line_per_file = math.ceil(line_count / n)

    file.seek(0, 0)
    base_name = './out/16_split_{}.txt'
    rest = list(range(0, line_count))
    for file_number in range(n):
        pick = rest[0:line_per_file]
        rest = rest[line_per_file:]
        with open(base_name.format(file_number), mode='w') as out:
            for line_number in pick:
                out.write(file.readline())
                # macのsplitコマンドはnオプションがない。。。
                # split -l 8 hightemp.txt ./out/16_bash_split.txt.

    file.close()


if __name__ == '__main__':
    main()
