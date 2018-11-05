#!/usr/bin/env python
import json
import re


def main():
    with open('out/england_article.json') as file:
        article = json.loads(file.readline())
        text = article.get('text')

    pattern = r'(==+)(\w*)==+'
    sections = re.findall(pattern, text)
    print(sections)
    leveled_sections = [(len(section[0]) - 1, section[1]) for section in sections]
    print(leveled_sections)
    for section in leveled_sections:
        print("{} {}".format(section[0], section[1]))


if __name__ == '__main__':
    main()
