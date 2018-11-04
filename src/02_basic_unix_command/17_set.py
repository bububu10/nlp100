#!/usr/bin/env python


def main():
    with open('./hightemp.txt') as file:
        first_col_set = set(line.split()[0] for line in file.readlines())
        print(first_col_set)  # sort -k 1 -t \t hightemp.txt | cut -f 1 | uniq


if __name__ == '__main__':
    main()
