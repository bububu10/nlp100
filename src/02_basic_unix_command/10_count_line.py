#!/usr/bin/env python


def main():
    with open('./hightemp.txt') as file:
        print(sum([1 for line in file]))  # wc hightemp.txt


if __name__ == '__main__':
    main()
