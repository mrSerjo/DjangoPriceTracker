from bs4 import BeautifulSoup
import lxml
import os

# path = os.getcwd()
# html = os.path.join(path, 'index.html')
# print(html)
#
# with open(html, 'r') as file:
#     body = file.read()

with open('index.html', 'r') as file:
    body = file.read()

soup = BeautifulSoup(body, 'lxml')
print(soup.prettify())

# get the title
title = soup.title
print(title)
print(title.name)
print(title.getText())