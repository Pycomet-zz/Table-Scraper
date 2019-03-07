#This Program is a reuse web scraping script 
#Scrape table details from a website

#This script is written in Python 3.7.1

#Importing the needed modules for the task
from bs4 import BeautifulSoup
import requests
import time

#Creating output file
with open ('Table.txt', 'w') as r:
    r.write('Trump Approval Index History Data\n')

url = '' # Input website url here

res = requests.get(url)
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.find('table', class_ = 'renderedtable')

    with open ('Table.txt', 'a') as r:
        for row in table.find_all('tr'):
            for cell in row.find_all('td'):
                r.write(cell.text.ljust(30))
            r.write('\n')
    r.close()
                             
else:
    print('No response')
