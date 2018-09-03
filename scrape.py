# -*- coding: utf-8 -*-

from lxml import html
import requests
import sys
import json

amount = int(raw_input("How many of the top movies do you want to get?\n"))

if amount % 50 != 0:
    amount = int(raw_input("Please type a number in steps of 50\n"))

pages = amount / 50
base_url = "https://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=simple&page="
all_titles = []

for idx in range(pages):
    url = "{}{}".format(base_url, idx)
    page = requests.get(url, headers={'Accept-Language': 'en-EN'}) # change your language here

    tree = html.fromstring(page.content)
    titles_arr = tree.xpath("//span[@class='lister-item-header']/span/a/text()")

    all_titles += titles_arr
    print("Scraping pages {}".format(idx))

with open("filme.json", 'wb') as outfile:
    json.dump(all_titles, outfile)
