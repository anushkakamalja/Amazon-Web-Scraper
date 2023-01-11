from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import csv
import pandas as pd

def check_price():
    URL= 'https://www.amazon.in/DUDEME-Programmer-Coding-Developer-T-Shirt/dp/B08SF73421/ref=sr_1_1?keywords=data%2Banalyst%2Btshirt&qid=1673419438&sprefix=data%2Banalyst%2Caps%2C245&sr=8-1&th=1&psc=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'lxml')
    soup2 = BeautifulSoup(soup1.prettify(), 'lxml')
    title = soup2.find('span', id='productTitle').text.strip()
    price = soup2. find('span', class_='a-offscreen').text.strip()[1:]
    ratings = soup2.find('a', class_='a-popover-trigger a-declarative').i.text.replace(' out of ','/').strip().replace('stars', '')
    today = datetime.date.today()
    data = [title, price, ratings, today]
    with open('Amazon Web Scraper Dataset.csv', 'a+', newline = '', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)



# print(f'Tilte: {title}')
# print(f'Price: {price}')
# print(f'Ratings: {ratings}')

header = ['Title', 'Price in Rs.', 'Ratings', 'Date']
with open('Amazon Web Scraper Dataset.csv', 'w', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    # writer.writerow(data)


while (True):
    check_price()
    timer = 1
    time.sleep(timer * 24*60*60)

# df = pd.read_csv(r"D:\coding\web scraping\Amazon-Web-Scraper\Amazon Web Scraper Dataset.csv")
# print(df)