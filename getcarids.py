# Get Car IDs

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-Language": "en-us, en;q=0.5"}

url = "https://www.classicbid.de/vehicle-type/convertible/"

results  = requests.get(url,headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

print(soup.prettify())

# Create the empty lists for data storage.

idnumber = []

car_div = soup.find_all('div', class_='single-vehicle-view view-list')

# For loop to pull from all of the div containers.

for container in car_div:
    carid = container.find('p', class_='btn-car-id').text
