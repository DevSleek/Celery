import requests

from celery import shared_task
from bs4 import BeautifulSoup

from app.models import House


@shared_task()
def test_task():
    data = requests.get("https://www.olx.uz/oz/nedvizhimost/doma/?view=list").text
    soup = BeautifulSoup(data, 'html.parser')

    for i in soup.find_all("div", class_="css-1apmciz"):
        title = i.a.text
        price = i.p.text
        # location_date = i.p.text

        house, _ = House.objects.get_or_create(title=title)
        house.price = price
        # house.location_date = location_date
        house.save()

