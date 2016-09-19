from bs4 import BeautifulSoup
import youtube_dl
import requests

url = 'http://www.heardontv.com/tvshow/'

def youtubelinks(title):
    youtubeurl = 'https://www.youtube.com/results?search_query=' + title
    site = requests.get(youtubeurl)
    soup = BeautifulSoup(site.text, "lxml")
    first_video = soup.select('ol.section-list ol.item-section a:nth-of-type(1)')
    newurl = 'https://www.youtube.com/' + first_video[0]['href']
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([newurl])

def allsongs(href):
    site = requests.get(href)
    soup = BeautifulSoup(site.text, "lxml")
    titles = soup.select("div.row-fluid div.song span.song_title")
    for song in titles:
        tag = song
        song_title = tag.string
        youtubelinks(song_title)

def getseasons(soup):
    seasons = soup.select("div.seasons a")
    for season in seasons:
        print season['href']
        getepisodes(season['href'])

def urlseries(series):
    link = url + series + '/'
    link = (link.replace(" ", "+")).lower()
    return link

def getepisodes(href):
    site = requests.get(href)
    soup = BeautifulSoup(site.text, "lxml")
    episodes = soup.select("div.episode_title a")
    for episode in episodes:
        print episode['href']
        allsongs(episode['href'])

def input():
    series = raw_input("Series: ")
    link = urlseries(series)
    site = requests.get(link)
    soup = BeautifulSoup(site.text, "lxml")
    getseasons(soup)

def main():
    input()


if __name__ == '__main__':
    main()