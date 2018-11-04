#!/usr/bin/env python


def text(x: int, y: str, z: float) -> str:
    return '{}時の{}は{}'.format(x, y, z)


def main():
    print(text(12, '気温', 22.4))


if __name__ == '__main__':
    main()
