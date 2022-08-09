from __future__ import annotations

import httpx
from typing import TypedDict, Optional


class Quote(TypedDict):
    author: str
    body: str
    tags: list[str]
    url: str


def get_quote_of_the_day() -> Optional[Quote]:
    try:
        response = httpx.get('https://favqs.com/api/qotd')
    except httpx.HTTPError as e:
        print('unable to get quote, reason:')
        print(e)
    else:
        if response.status_code >= 400:
            print('Huh, for some reason, we cannot find the quote')
            print('status code:', response.status_code)
            print('response:', response.text)
            return

        quote_data = response.json()['quote']
        return {
            'author': quote_data['author'],
            'body': quote_data['body'],
            'tags': quote_data['tags'],
            'url': quote_data['url'],
        }
