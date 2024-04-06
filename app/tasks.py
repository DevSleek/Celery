import requests

from bs4 import BeautifulSoup
from celery import shared_task

from app.models import House


@shared_task()
def test_task():
    html = requests.get("https://www.olx.uz/nedvizhimost/?page=").text
    soup = BeautifulSoup(html, "html.parser")

    posts = soup.find_all(attrs={"data-testid": "l-card"})
    for post in posts:
        title: str = post.find("h6").text
        price: str = (
            post.find(attrs={"data-testid": "ad-price"})
            .text.replace("Договорная", "")
            .replace("сум", "")
            .strip()
        )
        location: str = (
            post.find(attrs={"data-testid": "location-date"}).text.split(" - ")[0].strip()
        )
        area: str = post.find(attrs={"class": "css-1kfqt7f"}).text
        house, _ = House.objects.get_or_create(title=title)
        house.price = price
        house.location_date = location
        house.save()

