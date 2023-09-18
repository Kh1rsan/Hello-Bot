import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = 'https://colorscheme.ru/color-names.html'

r = requests.get(URL)

print(r.status_code)