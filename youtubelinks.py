from bs4 import BeautifulSoup
import requests
from download import download

def youtubelinks(title, path):
    youtubeurl = 'https://www.youtube.com/results?search_query=' + title
    site = requests.get(youtubeurl)
    soup = BeautifulSoup(site.text, "lxml")
    first_video = soup.select('ol.section-list ol.item-section a:nth-of-type(1)')
    newurl = 'https://www.youtube.com' + first_video[0]['href']
    download(newurl, path)