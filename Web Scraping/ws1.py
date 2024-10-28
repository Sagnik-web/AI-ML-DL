import requests

from bs4 import BeautifulSoup

import pandas as pd

url = "https://en.wikipedia.org/wiki/JavaScript"

response = requests.get(url)

print(response)



soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)


table_data = soup.find('table')

# print(table_data.find_all('tr'))

data = []

for row in table_data.find_all('td'):
    text = row.text
    data.append(text)

tr_data = []

for row in table_data.find_all('th'):
    text = row.text
    tr_data.append(text)

data.remove('')
data.remove('\n')
# print(tr_data)
# print(data)

new_data = {'Head': tr_data, 'Data': data[1:-2]}
df = pd.DataFrame(new_data)

print(df)
