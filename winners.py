import os
from bs4 import BeautifulSoup
import urllib
from lxml import html
import requests
import json
from termcolor import colored

PATH = '/Users/jp/Desktop/ICPC/winners/'


# Functions


def file_exist(filename):
    if not(os.path.isfile(filename)):
        print(filename)
        # print("File not exist")
        return False


# Read HTML files
def read_files(folder):
    if not os.path.exists(folder):
        print(colored("folder does not exist, please check.", 'yellow'))
    htmlfiles = [os.path.join(root, name)
                 for root, dirs, files in os.walk(folder)
                 for name in files
                 if name.endswith((".html", ".htm"))]
    return htmlfiles


# Crawling (Regional) winner table data
def get_tables(url):
    page = requests.get(url)
    page.encoding = page.apparent_encoding
    tree = html.fromstring(page.text)
    table_xpath = '//div[contains(@class, \'modal\')]//table'
    tables = tree.xpath(table_xpath)
    path = PATH+'/regional_winners.html'
    with open(path, mode="ab") as file:
        for table in tables:
            file.write(html.tostring(table))


def html_to_str(object):
    new_list = []
    if type(object) == 'list':
        for item in object:
            new_list.append(str(html.tostring(item)).decode())
        return new_list
    else:
        return str(html.tostring(object).decode())


def make_winner(year, data):
    print()


# Find all table, for each row (tr), extract information from all the column, make it to single column format.
def handle0(url):
    with open(url, "r") as f:
        page = f.read()
    f2 = open(PATH+"output.html", "a")
    
    tree = html.fromstring(page)
    teams = tree.xpath('//table//tr//td[1]//p[1]')
    members = tree.xpath('//table//tr//td[1]//p[position()>1]')
    photos = tree.xpath('//table//tr//td[2]')
    # Maybe make json object list: [{"team":"","members":"","photo":""},{"team":"","members":"","photo":""},...]
    # see: https://stackoverflow.com/questions/25348640/two-lists-to-json-format-in-python
    # Directly write
    for i in range(len(teams)):
        f2.write(html_to_str(teams[i]))
        for member in html_to_str(members[i]):
            f2.write(member)
        f2.write(html_to_str(photos[i]))
    f.close()
    f2.close()


def handle(url):
    with open(url, "r") as f:
        page = f.read()
    f2 = open(PATH + "output.html", "a")
    # Create template HTML
    output = f2.write("")
    # Get data by year
    # Insert the data of this year as a new record and write it to html


def main(url):
    htmlfiles = read_files(url)
    for html in htmlfiles:
        handle(html)


if not(file_exist('/Users/jp/Desktop/ICPC/winners/regional_winners.html')):
    get_tables("http://130.216.216.249/regional/regional-winners/")

main('/Users/jp/Desktop/ICPC/winners')
