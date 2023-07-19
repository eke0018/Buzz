import requests
from flask import Flask, render_template
import random


class Page:
    def __init__(self, title, author, date, text, image_url):
        self.title = title
        self.author = author
        self.date = date
        self.text = text
        self.image_url = image_url


def get_pages():
    # Demo key: pub_26214bb27e5391ccf65a4093eee07cbdd0d19
    # pub_262158950764bda6c85bd660f7f96bfca9075
    api_key = "pub_26214bb27e5391ccf65a4093eee07cbdd0d19"
    keywords = ["Sports", "Music", "Food", "Party",  "Money"]
    pages = []

    for keyword in keywords:
        url = f"https://newsdata.io/api/1/news?apikey={api_key}&q={keyword}&language=en"

        response = requests.get(url)
        data = response.json()

        if 'results' in data:
            i = random.randint(0, 9)
            page = Page(
                title=data['results'][i]['title'] or "Not Available",
                author=data['results'][i]['creator'] or "Anonymous",
                date=data['results'][i]['pubDate'] or "Not Available",
                text=data['results'][i]['content'] or "Not Available",
                image_url=data['results'][i]['image_url'] or "../static/images/buzzlogobig.png"
            )
            pages.append(page)

    return pages
