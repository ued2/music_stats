import csv
import pandas 
import glob

platform = input('Enter letter of Platform (A)Apple Music (B)Billboard (S)Spotify: ').strip()

name = input('Enter Artist: ').strip()


if platform == 'A':
    data = pandas.read_csv('AppleMusic.csv',  delimiter=',', names = ['rank', 'artist', 'song'])
elif platform == 'B':
    data = pandas.read_csv('BillboardTop100.csv',  delimiter=',', names = ['rank', 'artist', 'song'])
elif platform == 'S':
    data = pandas.read_csv('Spotify.csv',  delimiter=',', names = ['rank', 'artist', 'song', 'stream'])


def look(name,platform):
    print(data[data.artist == str(name)])
    print(data[data.artist == str(name)][['song']].count())
    #print(data.groupby('artist')['song'].count())

look(name,platform)