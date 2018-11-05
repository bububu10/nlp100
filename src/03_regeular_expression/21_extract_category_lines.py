#!/usr/bin/env python
import json
import re


def main():
    with open('out/england_article.json') as file:
        article = json.loads(file.readline())
        text = article.get('text')
        print(text)

    pattern = r'\[\[Category:.*\]\]'
    categories = re.findall(pattern, text)
    for category in categories:
        print(category)


if __name__ == '__main__':
    main()
