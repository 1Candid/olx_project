import time
import random

import requests
import telebot

from datetime import datetime, timedelta
from requests import get
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from itertools import chain

url = 'https://www.olx.pl/d/elektronika/telefony/smartfony-telefony-komorkowe/q-google-pixel-6/?search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=900&search%5Bfilter_float_price:to%5D=2000&search%5Bfilter_enum_state%5D%5B0%5D=new'
items = []      #list of data about every item
count = 1
gathered_data = []      #list of items from the link
list_products = []      #list of filtred items
item_info = []      #info about certain item
bot = telebot.TeleBot('6034447670:AAECXvSS3NPjf8Vd047p3F_lc_qjXEXpWEk')
#'https://www.olx.pl/d/elektronika/gry-konsole/konsole/playstation/' + '?page=' + str(count) + '&search%5Border%5D=created_at:desc'

while True:
    class Data_text:
        while count < 4:
            if count == 1:
                url = url
            elif count == 2:
                url = 'https://www.olx.pl/d/elektronika/komputery/laptopy/apple/wroclaw/?search%5Border%5D=created_at:desc'
            elif count == 3:
                url = 'https://www.olx.pl/d/elektronika/gry-konsole/konsole/playstation/wroclaw/?search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=590'
            print(url)
            response = get(url)
            html_soup = BeautifulSoup(response.text, 'html.parser')

            things_data = html_soup.find_all('div', class_="css-1sw7q4x")
            if things_data != []:
                items.extend(things_data)
                value = random.random()
                scaled_value = 1 + (value * (9 - 5))
                print(scaled_value)
                time.sleep(scaled_value)
            else:
                print('empty')
                break
            count += 1

    print(len(items), '- items in the list')

    class Product:

        list_len = int(len(items)) - 1
        count = 0

        while count < list_len:
            info = items[int(count)]

            if 'position:-webkit-sticky;position:sticky' in str(info):
                count += 1
                continue

            title = info.find('h6', {'class': 'css-16v5mdi er34gjf0'}).text
            price = info.find('p', {'class': 'css-10b0gli er34gjf0'}).text
            day = info.find('p', {'class': 'css-veheph er34gjf0'}).text
            item_url = 'https://www.olx.pl' + items[count].find('a').get('href')
            data = (title, price, day, item_url)
            count += 1

            gathered_data.append(data)

    class PastMoment:
        past_minutes = 65

        past_time = datetime.now() - timedelta(minutes=past_minutes)
        print(past_time.strftime("%H:%M"))
        print()

    class Filter:
        for i in gathered_data:
            if 'dzisiajo' + str(PastMoment.past_time.strftime("%H:%M")) in str(i).lower().replace(' ', ''):
                print(i)
                list_products.append(i)

#possibility of saving information in Excel
    '''class Excel:
        fn = 'scrap.xlsx'
        wb = load_workbook(fn)
        ws = wb['data']

        for data_imp in list_products:
            ws.append(data_imp)

        wb.save(fn)
        wb.close()'''

    #print('https://www.olx.pl' + items[1].find('a').get('href'))
    print(list_products)

    list_products = list(chain(*list_products))

    class TeleBot:
        for j in range(0, len(list_products) - 3, 4):
            for l in list_products[j:j + 4]:
                item_info.append(l)
            tg_item = '\n'.join(item_info)
            bot.send_message(559209074, tg_item)
            item_info = []

    list_products = []
    gathered_data = []
    items = []
    item_info = []

    time.sleep(50)