#!/usr/bin/env python


def cipher(plain: str) -> str:
    seq = [chr(219 - ord(char)) if (char.islower()) else char for char in plain]
    return "".join(seq)


def main():
    origin = 'I am a cat.'
    print('origin: ' + origin)
    encrypt = cipher(origin)
    print('encrypt: ' + encrypt)
    decrypt = cipher(encrypt)
    print('decrypt: ' + decrypt)


if __name__ == '__main__':
    main()
