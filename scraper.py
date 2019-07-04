import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.in/Apple-iPhone-XR-64GB-Blue/dp/B07JHQCYWR'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def send_email():
    pass


def check_price():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = int(price[2:4])

    if converted_price < 50:
        send_email()