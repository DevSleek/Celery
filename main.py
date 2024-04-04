import requests

from celery import shared_task
from bs4 import BeautifulSoup

# from app.models import House

data = requests.get("https://www.olx.uz/oz/nedvizhimost/doma/?view=list").text
soup = BeautifulSoup(data, 'html.parser')

for i in soup.find_all("div", class_="css-1apmciz"):
    for j in soup.find_all("div", class_="css-odp1qd"):
        location = j.p.text
    title = i.a.text
    price = i.p.text

    house, _ = House.objects.get_or_create(title=title)
    house.price = price
    house.location = location
    house.save()

