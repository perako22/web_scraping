import time
#from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


def scrape():
    browser = webdriver.Chrome('chromedriver.exe')
    listings = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.get(url)
    time.sleep(1)

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    listings["title"] = soup.find("a", class_="content_title").get_text()
    listings["teaser"] = soup.find("div", class_="article_teaser_body").get_text()

    return listings
