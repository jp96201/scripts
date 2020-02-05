# Remove all the links that not available in the Score Board HTML

import os
from chardet import detect
from termcolor import colored
from bs4 import BeautifulSoup

"""
Remove all href
"""


# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']


def file_exist(filename):
    if not(os.path.isfile(filename)):
        print(filename)
        print("File not exist")


def remove_tags(url):
    err = 0
    try:
        handle(url)
    except UnicodeDecodeError:
        err = err + 1
        print(colored("\n"+url+" is passed because of Decode error.", 'yellow'))
    return err


def handle(url):
    data = open(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    invalid_tags = ['a']
    for tag in invalid_tags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()
    with open(url, mode="w", errors='ignore') as file:
        file.write(str(soup.prettify()))


# get all src and href
folder = '/Users/mac/Desktop/ICPC/scoreBoards'
if not os.path.exists(folder):
    print(colored("folder does not exist, please check.", 'yellow'))


htmlfiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(folder)
             for name in files
             if name.endswith((".html", ".htm"))]

fail = 0
count = 0
for html in htmlfiles:
    count = count + 1
    print(html)
    fail = fail + remove_tags(html)
    print("Remove Done.")

print("\n")
result = str(count-fail)+"/"+str(count)+" has been removed a tags."
print(colored(result,'green'))
