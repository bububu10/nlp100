#!/usr/bin/env python


def main():
    col1_out = open('./out/col1.txt', mode='w')
    col2_out = open('./out/col2.txt', mode='w')

    with open('./hightemp.txt') as file:
        for line in file:
            cols = line.split('\t')
            col1_out.write(cols[0] + '\n')  # cat hightemp.txt | cut -f 1
            col2_out.write(cols[1] + '\n')  # cat hightemp.txt | cut -f 2

    col1_out.close()
    col2_out.close()


if __name__ == '__main__':
    main()
