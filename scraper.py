import requests
from bs4 import BeautifulSoup
import smtplib
import json
import time

url = 'https://www.amazon.in/Apple-iPhone-XR-64GB-Blue/dp/B07JHQCYWR'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    with open('auth.json', 'r') as f:
        auth = json.load(f)

    server.login(auth['username'], auth['password'])

    subject = 'Price Fell Down!'
    body = 'Check the link: https://www.amazon.in/Apple-iPhone-XR-64GB-Blue/dp/B07JHQCYWR'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'sudhanshuojha2009@gmail.com',
        'sudhanshuojha2009@gmail.com',
        msg
    )
    server.quit()


def check_price():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = int(price[2:4])

    print(title, converted_price)

    if converted_price > 50:
        send_email()


while(True):
    check_price()
    time.sleep(60)

