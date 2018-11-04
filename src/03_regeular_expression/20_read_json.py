#!/usr/bin/env python
import gzip
import json


def main():
    with gzip.open('jawiki-country.json.gz', mode='rb') as file:
        article = [json.loads(line) for line in file if json.loads(line).get('title') == 'イギリス'][0]
        print(article.get('text'))
        with open('out/england_article.json', mode='w') as out:
            json.dump(article, out, ensure_ascii=False)


if __name__ == '__main__':
    main()
