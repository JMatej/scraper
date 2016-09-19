from scraper import getseasons
from bs4 import BeautifulSoup
import requests

url = 'http://www.heardontv.com/tvshow/'

def main():
    series = raw_input("Series: ")
    link = url + series + '/'
    link = (link.replace(" ", "+")).lower()
    site = requests.get(link)
    soup = BeautifulSoup(site.text, "lxml")
    path = r'/home/matej/Documents/scraper-matej/' + series + '/'
    getseasons(soup, path)

if __name__ == '__main__':
    main()