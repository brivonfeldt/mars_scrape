from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/briv1/OneDrive/Documents/GitHub/Assignment_Master/UDEN201902DATA4-master/12-Web-Scraping/Homework_Instructions"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    article_title_list = soup.select('li.slide .content_title')
    article_content_list = soup.select('li.slide .article_teaser_body')
  

    return listings
