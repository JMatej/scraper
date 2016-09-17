from bs4 import BeautifulSoup
import requests

def allsongs():
    listSongs = []
    titles = soup.select("div.row-fluid div.song span.song_title")
    for song in titles:
        tag = song
        correct = tag.string
        correct.replace(" ", "")
        listSongs.append(correct)
    return listSongs

def urlseries(series, season, episode):
    a = 'http://www.heardontv.com/tvshow/'
    url = a + series + '/Season+' + season + '/' + episode
    url = (url.replace(" ", "+")).lower()
    return url

def input():
    series = raw_input("Series: ")
    season = raw_input("Season: ")
    episode = raw_input("Episode: ")
    url = urlseries(series, season, episode)
    return url

url = input()
site = requests.get(url)
soup = BeautifulSoup(site.text, "lxml")
# print soup.prettify()
songs = allsongs()
for song in songs:
    print song