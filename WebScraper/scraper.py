import requests
from bs4 import BeautifulSoup
import json
URL = 'https://www.gasbuddy.com/usa'
page = requests.get(URL)

find_ohio = ''
ohio_gas_price = 0

path = 'C:/'
filename = 'OhioGasPrice.json'
data = {}

soup = BeautifulSoup(page.content, 'html.parser')
find_ohio = soup.find('a', { "id" : "OH" })
ohio_gas_price = find_ohio.find('div', {"class" : "col-sm-2 col-xs-3 text-right"}).getText()
print(ohio_gas_price.strip())
data = ohio_gas_price.strip()

j = json.dumps(data)
with open('OhioGasPrice.json', 'w') as f:
    f.write(j)
    f.close