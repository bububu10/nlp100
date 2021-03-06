#!/usr/bin/env python


def main():
    # TODO メモリにすべてのデータを抱えるのでファイルが大きいと破綻する？
    col1 = open('./out/col1.txt')
    col1_lines = [line.rstrip() for line in col1.readlines()]
    print(col1_lines)
    col1.close()

    col2 = open('./out/col2.txt')
    col2_lines = [line.rstrip() for line in col2.readlines()]
    print(col2_lines)
    col2.close()

    with open('./out/merged_col1_col2.txt', mode='w') as out:
        zipped = list(zip(col1_lines, col2_lines))
        for line in zipped:
            out.write("{}\t{}\n".format(line[0], line[1]))  # paste out/col1.txt out/col2.txt


if __name__ == '__main__':
    main()
