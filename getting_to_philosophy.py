# -*- coding: utf-8 -*-
"""
@author: Menna El-Zahaby

"""

import time
import urllib
import bs4
import requests

startLink = "https://en.wikipedia.org/wiki/Special:Random"
targetLink = "https://en.wikipedia.org/wiki/Philosophy"

def get_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="mw-content-text")
    # stores the first link found in the article, if the article contains no links this value will remain None
    found_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p"):
        
        # Find the first anchor tag that's a direct child of a paragraph.
        if element.find("a"):
            found_link = element.find("a").get('href')
            break

    if not found_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', found_link)

    return first_link

def crawling_func(history, target_url, max_steps=25):
    if history[-1] == target_url:
        print (history[-1])
        print("Philosophy article reached!")
        return False
    elif len(history) > max_steps:
        print("Too many search times, End search")
        return False
    elif history[-1] in history[:-1]:
        print("We seem to enter a loop, End search")
        return False
    else:
        return True

articles_list = [startLink]

while crawling_func(articles_list, targetLink):
    print(articles_list[-1])

    first_link = get_first_link(articles_list[-1])
    if not first_link:
        print("No links found, search ended!")
        break

    articles_list.append(first_link)

    time.sleep(0.5) 