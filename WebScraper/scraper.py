import requests
from bs4 import BeautifulSoup
import json
#from firebase import firebase
URL = 'https://www.gasbuddy.com/usa'
page = requests.get(URL)

#item_name_list = []
#item_sku_list = []
#item_img_address_list = []
#temp_int_one = 0
state_list = []
ohio_gas_price = 0

path = 'C:/'
filename = 'test1.json'
data = {}

soup = BeautifulSoup(page.content, 'html.parser')
state_list = soup.find('div', class_='row')
item_sku_list = soup.find_all('div', class_='sku')




print(data)

j = json.dumps(data)
with open('test1.json', 'w') as f:
    f.write(j)
    f.close