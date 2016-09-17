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
    episode = a + series + '/Season+' + season + '/' + episode
    episode = (episode.replace(" ", "+")).lower()
    return episode

series = raw_input("Series: ")
season = raw_input("Season: ")
episode = raw_input("Episode: ")
url = urlseries(series, season, episode)
site = requests.get(url)
soup = BeautifulSoup(site.text, "lxml")
# print soup.prettify()
songs = allsongs()
for song in songs:
    print song