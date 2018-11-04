#!/usr/bin/env python


def main():
    with open('./out/11_out.txt', mode='w') as out:
        with open('./hightemp.txt') as file:
            for line in file:
                out.write(line.replace('\t', ' '))  # cat hightemp.txt | sed s/$'\t'/' '/g > ./out/11_sed_out.txt


if __name__ == '__main__':
    main()



