# -*- coding: utf-8-sig -*-
import requests
from bs4 import BeautifulSoup
import csv

CSV = 'clothes.csv'
HOST = 'https://www.wildberries.ru/'
URL = 'https://www.wildberries.ru/catalog/muzhchinam/odezhda/dzhinsy'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                     'image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='dtList-inner')
    clothes = []
    for item in items:
        clothes.append({
            'title': item.find('span', class_='goods-name').get_text(strip=True),
            'link': HOST + item.find('a', class_='ref_goods_n_p').get('href'),
            'brand': item.find('strong', class_='brand-name').get_text(strip=True),
            'card_img': HOST + item.find('div', class_='l_class').find('img').get('src'),
            'price': item.find('span', class_='price').get_text(strip=True).replace(u'\xa0', '')
        })
    return clothes


def create_csv(items, path):
    with open(path, 'w', newline='', encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название продукта', 'Ссылка', 'Брэнд', 'Картинка', 'Цена'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['brand'], item['card_img'], item['price']])


def parse():
    QUESTION = input('Укажите количество страниц для парсинга: ')
    QUESTION = int(QUESTION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        clothes = []
        for page in range(1, QUESTION):
            print(f'Парсинг страницы: {page}')
            html = get_html(URL, params={'page': page})
            clothes.extend(get_content(html.text))
            create_csv(clothes, CSV)
        print(clothes)
    else:
        print('Error')


parse()
