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

from bs4 import BeautifulSoup


def load_webpage(page):
    """
    :param: page: webpage url

    :return: BS html file
    """
    with open(page, "r") as f:
        return BeautifulSoup(f, "html.parser")


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


# load Apache2 server webpage
web_page = "apache2_webserver.html"
html_file = load_webpage(web_page)

# find headings of HTML file
headers = find_headings(html_file)

# count occurrences of word in HTML file
search_word = "Apache2"
occurrences = word_occurrences(html_file, search_word)

# dictionary to display headers, word count and ...
my_dict = {"Headers": headers,
           "Word occurrences": occurrences}

print(my_dict)
