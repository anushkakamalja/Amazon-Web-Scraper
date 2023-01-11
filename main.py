from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

URL= 'https://www.amazon.in/DUDEME-Programmer-Coding-Developer-T-Shirt/dp/B08SF73421/ref=sr_1_1?keywords=data%2Banalyst%2Btshirt&qid=1673419438&sprefix=data%2Banalyst%2Caps%2C245&sr=8-1&th=1&psc=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'lxml')
soup2 = BeautifulSoup(soup1.prettify(), 'lxml')
title = soup2.find('span', id='productTitle').text.strip()
price = soup2. find('span', class_='a-offscreen').text.strip()
ratings = soup2.find('a', class_='a-popover-trigger a-declarative').i.text.replace(' out of ','/').strip().replace('stars', '')
print(f'Tilte: {title}')
print(f'Price: {price}')
print(f'Ratings: {ratings}')