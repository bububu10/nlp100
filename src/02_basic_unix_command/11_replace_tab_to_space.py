#!/usr/bin/env python


def main():
    out = open('./out/11_out.txt', mode='w')
    with open('./hightemp.txt') as file:
        for line in file:
            out.write(line.replace('\t', ' '))  # cat hightemp.txt | sed s/$'\t'/' '/g
    out.close()


if __name__ == '__main__':
    main()
