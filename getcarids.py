# Get Car IDs

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://www.glenmarch.com/auctions/results/1103?limit=9999"
# headers = {"Accept-Language": "en-us, en;q=0.5"}
# results  = requests.get(url,headers=headers)
results  = requests.get(url)
soup = BeautifulSoup(results.text, "html.parser")

# Create the empty lists for data storage.

lotname = []

car_div = soup.find_all('div', class_='make extra-top')

# For loop to pull from all of the div containers.

for container in car_div:
    carname = container.font
    lotname.append(carname)

print(lotname)

