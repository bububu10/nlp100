#!/usr/bin/env python
import json
import re


def main():
    with open('out/england_article.json') as file:
        article = json.loads(file.readline())
        text = article.get('text')
        # print(text)

    pattern = r'\[\[(ファイル|File|file):(.*?)\|.*\]\]'
    files = re.findall(pattern, text, )
    # print(files)

    file_names = [file[1] for file in files]
    for file_name in file_names:
        print(file_name)


if __name__ == '__main__':
    main()
