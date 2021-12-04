"""
#
#   File        :   web_scrape.py
#   Created     :   24/11/2021 22:27
#   Author      :   Ciarán Ó hÓgáin
#   Version     :   v1.0
#   Description :   Using Python to web scrape the default page
#                   of Apache2 web server being run on VM.
#
"""
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from PIL import Image
import pprint


# load and parse html file of webpage
def load_webpage(page):
    """
    :param: page: webpage url

    :return: BS html file
    """
    return BeautifulSoup(page, "html.parser")


# find headings of loaded html file using section_header class
def find_headings(file):
    """

    :param: file: html file of webpage

    :return: list of headers in HTML file
    """
    tags = file.find_all(class_="section_header")
    headings = []

    for tag in tags:
        headings.append(tag.text.strip())

    return headings


# count occurrences of word in loaded html file
def word_occurrences(file, word):
    """

    :param file: html file of webpage
    :param word: Word to search occurrences for

    :return count: Number of occurrences of given word
    """
    count = 0
    tags = file.find_all(["span", "p", "b", "tt", "pre", "li"])

    for tag in tags:
        count += str(tag).upper().count(word.upper())

    return count


# scrapes and returns source of first image in webpage
def scrape_image(file, url):
    """

    :param url:
    :param file: html file of webpage
    :return img_url: url to first image in webpage
    """
    img_src = file.find("img").attrs['src']
    img_url = url+img_src

    return img_url


# load Apache2 server webpage
web_page = "http://192.168.0.59"
html_file = load_webpage(requests.get(web_page).content)

# find headings of HTML file
headers = find_headings(html_file)

# count occurrences of word in HTML file
search_word = "Apache2"
occurrences = word_occurrences(html_file, search_word)

# scrape image
img_src_url = scrape_image(html_file, web_page)

# display image using Pillow package
response = requests.get(img_src_url)
img = Image.open(BytesIO(response.content))
img.show()

# dictionary to display headers, word count and ...
my_dict = {"Headers": headers,
           "Word occurrences": occurrences,
           "Image source": img_src_url}

# pretty print dictionary using pprint package
pprint.pprint(my_dict)
