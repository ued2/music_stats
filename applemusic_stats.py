from bs4 import BeautifulSoup
import requests
import csv
import time
import random

then = time.time()

# creating csv file for apple music list

a_csv_file = open('AppleMusic.csv', 'w')
a_csv_writer = csv.writer(a_csv_file)
a_csv_writer.writerow(['Rank', 'Artist', 'Song'])

# url link for apple music
a_link = 'https://kworb.net/charts/apple_s/us.html'

# query the apple music website and return the html
a_page = requests.get(a_link).text

# convert apple music website to beautifulSoup
a_soup = BeautifulSoup(a_page, 'html.parser')

# apple music list
a_list = a_soup.find('tbody')


# all apple music artist names
a_all_artist = a_list.find_all(class_='mp text')
a_artist_list = []

# putting apple music artist in a list
for artist in a_all_artist:
    temp = artist.text.split('-')
    a_artist_list.append(temp[0].strip())


# all apple music song names
a_all_song = a_list.find_all(class_='mp text')
a_song_list = []

# putting apple music song in a list
for song in a_all_song:
    temp = song.text.split('-')
    a_song_list.append(temp[1].strip())

# putting apple music artist and song into csv file
i = 0
while i < len(a_artist_list):
    a_csv_writer.writerow([i+1, a_artist_list[i], a_song_list[i]])
    i = i + 1

# counting number of times artist appears on apple music list
x = 0
a_count_list = []
while x < len(a_artist_list):
    a_count_list.append((a_artist_list[x] + ' appears ' + str(
        a_artist_list.count(a_artist_list[x])) + ' times on the Apple Music Charts'))
    x = x + 1

a_final_count_list = list(set(a_count_list))
a_new_count_list = sorted(a_final_count_list, reverse=False)
#print(*a_new_count_list, sep='\n')

# turns lists into dictionary {artist:song}


def Convert(lst, lst2):
    res_dct = {lst[i]: lst2[i] for i in range(0, len(lst), 1)}
    return res_dct


mix = Convert(a_artist_list, a_song_list)


now = time.time()

print('Done creating Apple Music List ... Took ' + str(now-then) + ' seconds')
