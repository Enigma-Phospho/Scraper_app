from bs4 import BeautifulSoup
import requests
import time

my_url = requests.get(
    'https://www.newegg.com/ibuypower-slate5mr-216i/p/N82E16883227949?Item=N82E16883227949&cm_sp=Gametober-_-1012-1018-_-83-227-949-_-NA').text

soup = BeautifulSoup(my_url, "lxml")


def rig_price_checker(url):
    price_tags = soup.find("ul", class_="price")
    price_li_tag = price_tags.find("li", class_="price-current")
    rig_price = price_li_tag.find("strong")
    print(rig_price.string)
