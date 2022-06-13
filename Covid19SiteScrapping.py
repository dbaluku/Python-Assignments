import requests
import lxml.html as lh
import pandas as pd 
import numpy as np

url = 'https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases'
whole_page = requests.get(url)
doc = lh.fromstring(whole_page.content)
print(doc)

