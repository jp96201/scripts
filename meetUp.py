import urllib
from lxml import html
import requests
import json

# Find specific meetup user's activity
# 1. find people... (member number) and his/her groups
number = str(input("Input the member ID:"))
url = "https://www.meetup.com/members/" + number + "/groups"
# 2. parsing
page = requests.get(url)
page.encoding = page.apparent_encoding
tree = html.fromstring(page.text)
# This will create a list of groups:
group_elements = tree.xpath('//div[@id=\'my-meetup-groups-list\'][1]//h4/a')
# groups = {'group_name': [], 'group_link': []}
group_title = []
group_link = []
groups = {}

for group in group_elements:
    group_title.append(group.text.strip())  # key
    group_link.append(group.get('href'))  # value
    groups = dict(zip(group_title, group_link))
# print the groups dict
print(
   json.dumps(groups, indent=None,
              separators=(',\n', ': ')).encode().decode('unicode-escape'))
# 3. each meetup: list all upcoming events:
# for loop all groups:
for k, v in groups.items():
    url_group = str(v) + "events/"
    page = requests.get(url_group)
    page.encoding = page.apparent_encoding
    tree = html.fromstring(page.text)
    # Nearest 5 upcoming events for current group
    upcomings = tree.xpath(
        "(//div[@class='card card--hasHoverShadow eventCard border--none border--none buttonPersonality'])"
        "[position()<6]/a/@href")
    # for loop all upcomings for each group:
    for u in upcomings:
        attendees_url = "https://www.meetup.com" + u + "attendees/"
        print(attendees_url)
        page = requests.get(attendees_url)
        page.encoding = page.apparent_encoding
        tree = html.fromstring(page.text)
        print(html.tostring(tree))
        attendees_name = tree.xpath('//li[@class=\'attendee-item list-item\']//h4/text()')
        print(attendees_name)
