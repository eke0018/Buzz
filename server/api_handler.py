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
    api_key = "pub_262158950764bda6c85bd660f7f96bfca9075"
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


def location():
    api_key = "34d1f9987459489c849fd220117949c1"
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    return data['ip']


def get_weather():
    api_key = "1e5def7da66f4898a5940134233006"
    ip_address = location()
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ip_address}"

    response = requests.get(url)
    data = response.json()
    print(data)
    weather = []
    weather.append(data['location']['name'])
    weather.append(data['location']['region'])
    weather.append(data['location']['country'])
    weather.append(data['current']['temp_c'])
    weather.append(data['current']['feelslike_c'])
    weather.append(data['current']['temp_f'])
    weather.append(data['current']['feelslike_f'])
    weather.append(data['current']['condition']['text'])

    return weather
