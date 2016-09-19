from bs4 import BeautifulSoup
import requests
import os
from youtubelinks import youtubelinks

def getseasons(soup, path):
    seasons = soup.select("div.seasons a")
    for season in seasons:
        season_title = season.text
        newseason = path + season_title + '/'
        os.makedirs(newseason)
        getepisodes(season['href'], newseason)

def getepisodes(href, season):
    site = requests.get(href)
    soup = BeautifulSoup(site.text, "lxml")
    episodes = soup.select("div.episode_title a")
    for episode in episodes:
        episode_title = episode.text
        newepisode = season + episode_title
        os.makedirs(newepisode)
        allsongs(episode['href'], newepisode)

def allsongs(href, path):
    site = requests.get(href)
    soup = BeautifulSoup(site.text, "lxml")
    titles = soup.select("div.row-fluid div.song span.song_title")
    for song in titles:
        tag = song
        song_title = tag.string
        youtubelinks(song_title, path)