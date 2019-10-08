import requests
from bs4 import BeautifulSoup
import csv

import time
import random

then = time.time()

#creating csv file 

csv_file = open('BillboardTop100.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank','Artist','Song'])

#url link 
link = 'https://www.billboard.com/charts/hot-100'

#query the website and return the html 
page = requests.get(link).text

#convert to beautifulSoup
soup = BeautifulSoup(page, 'html.parser')


#billboard list ele
list_ele = soup.find(class_='chart-list__elements')

#all rank number
all_rank = list_ele.find_all(class_='chart-element__rank__number')
rank_list = []

#all artist names
all_artist = list_ele.find_all(class_='chart-element__information__artist text--truncate color--secondary')
artist_list = []

#all song names
all_song = list_ele.find_all(class_='chart-element__information__song text--truncate color--primary')
song_list = []

#putting artist in a list 
for artist in all_artist:
	artist_list.append(artist.text.strip())

#putting song in a list 
for song in all_song:
	song_list.append(song.text.strip())


#putting artist and song into csv file 
i=0
while i < 100:
	csv_writer.writerow([i+1,artist_list[i],song_list[i]])
	i = i + 1

#counting number of times artist appears on list
x=0
count_list = []
while x < len(artist_list):
	count_list.append((artist_list[x] +' appears '+ str(artist_list.count(artist_list[x])) +' times on the Billboard Charts'))
	x = x + 1

final_count_list = list(set(count_list))
new_count_list = sorted(final_count_list, reverse=False)
print(*new_count_list, sep='\n')

now = time.time()

print('Done creating Billboard Music List ... Took '+ str(now-then) + ' seconds')

