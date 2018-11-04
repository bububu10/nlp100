#!/usr/bin/env python


def main():
    with open('./hightemp.txt') as file:
        lines = [line.split() for line in file.readlines()]
        sorted_lines = sorted(lines, key=lambda cols: cols[2], reverse=True)
        for line in sorted_lines:
            print('\t'.join(line))  # sort -k 3 -t $'\t' -r hightemp.txt


if __name__ == '__main__':
    main()
