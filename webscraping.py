import requests
from bs4 import BeautifulSoup
from csv import writer


def getInfo(barcode):
    response = requests.get('https://www.upcdatabase.com/item/0012345678905')

    soup = BeautifulSoup(response.content, 'html.parser')

    data = []
    table = soup.find('table', attrs={'class':'data'})

    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    return data



