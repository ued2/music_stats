import csv
import pandas 

platform = input('Enter letter of Platform (A)Apple Music (B)Billboard (S)Spotify: ')
name = input('Enter Artist: ')


if platform == 'A':
    Platform = pandas.read_csv('AppleMusic.csv',  delimiter=',', names = ['rank', 'artist', 'song'])
elif platform == 'B':
    Platform = pandas.read_csv('BillboardTop100.csv',  delimiter=',', names = ['rank', 'artist', 'song'])
elif platform == 'S':
    Platform = pandas.read_csv('Spotify.csv',  delimiter=',', names = ['rank', 'artist', 'song', 'stream'])


def look(name,platform):
    print(Platform[Platform.artist == str(name.strip())])
    print(Platform[Platform.artist == str(name.strip())][['song']].count())

look(name,platform)