#!/usr/bin/env python
import json


def main():
    with open('jawiki-country.json') as file:
        article = [json.loads(line) for line in file if json.loads(line).get('title') == 'イギリス'][0]
        print(article.get('text'))


if __name__ == '__main__':
    main()
