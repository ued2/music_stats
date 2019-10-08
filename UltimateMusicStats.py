from bs4 import BeautifulSoup
import requests
import csv
import time
import random

then = time.time()
#creating csv file for Apple Music List
a_csv_file = open('AppleMusic.csv','w')
a_csv_writer = csv.writer(a_csv_file)
a_csv_writer.writerow(['Rank','Artist','Song'])

#creating csv file for Billboard List
b_csv_file = open('BillboardTop100.csv','w')
b_csv_writer = csv.writer(b_csv_file)
b_csv_writer.writerow(['Rank','Artist','Song'])

#creating csv file for Spotify List
s_csv_file = open('Spotify.csv','w')
s_csv_writer = csv.writer(s_csv_file)
s_csv_writer.writerow(['Rank','Artist','Song','Streams'])

#url link for apple music,billboard,spotify

link = {
	'applemusic': ('https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12'),
	'billboard' : ('https://www.billboard.com/charts/hot-100'),
	'spotify': ('https://spotifycharts.com/regional/us/daily/latest') 
}

#query the apple music,billboard & spotify website and return the html 
page = {
	'applemusic': (requests.get(link['applemusic']).text),
	'billboard' : (requests.get(link['billboard']).text),
	'spotify': (requests.get(link['spotify']).text) 
}


#convert apple music,billboard,spotify website to beautifulSoup
soup = {
	'applemusic': (BeautifulSoup(page['applemusic'], 'html.parser')),
	'billboard': (BeautifulSoup(page['billboard'], 'html.parser')),
	'spotify': (BeautifulSoup(page['spotify'], 'html.parser'))
}

#apple music,billboard,spotify list 
List = {
	'applemusic': (soup['applemusic'].find(class_='product-hero__tracks')),
	'billboard': (soup['billboard'].find(class_='chart-list__elements')),
	'spotify': (soup['spotify'].find(class_='chart-table'))
} 

#timer for apple music code 
a_then = time.time()

#all apple music artist names
a_all_artist = List['applemusic'].find_all(class_='table__row__link table__row__link--secondary')
a_artist_list = []

#putting apple music artist in a list 
for artist in a_all_artist:
	a_artist_list.append(artist.text.strip())

#all apple music song names
a_all_song = List['applemusic'].find_all(class_='we-truncate we-truncate--single-line ember-view tracklist-item__text__headline targeted-link__target')
a_song_list = []

#putting apple music song in a list 
for song in a_all_song:
 	a_song_list.append(song.text.strip())

#putting apple music artist and song into csv file 
i=0
while i < 100:
	a_csv_writer.writerow([i+1,a_artist_list[i],a_song_list[i]])
	i = i + 1

#counting number of times artist appears on apple music list
x=0
a_count_list = []
while x < len(a_artist_list):
	a_count_list.append((a_artist_list[x] +' appears '+ str(a_artist_list.count(a_artist_list[x])) +' times on the Apple Music Charts'))
	x = x + 1

a_final_count_list = list(set(a_count_list))
a_new_count_list = sorted(a_final_count_list, reverse=False)
print(*a_new_count_list, sep='\n')

#timer for apple music code 
a_now = time.time()

print('Done creating Apple Music List ... Took '+ str(a_now-a_then) + ' seconds')
print('--------------------------------------------------------------------')

#timer for billboard code 
b_then = time.time()

#all billboard artist names
b_all_artist = List['billboard'].find_all(class_='chart-element__information__artist text--truncate color--secondary')
b_artist_list = []

#all billboard song names
b_all_song = List['billboard'].find_all(class_='chart-element__information__song text--truncate color--primary')
b_song_list = []

#putting billboard artist in a list 
for artist in b_all_artist:
	b_artist_list.append(artist.text.strip())

#putting billboard song in a list 
for song in b_all_song:
	b_song_list.append(song.text.strip())

#putting billboard artist and song into csv file 
i=0
while i < 100:
	b_csv_writer.writerow([i+1,b_artist_list[i],b_song_list[i]])
	i = i + 1

#counting number of times artist appears on billboard list
x=0
b_count_list = []
while x < len(b_artist_list):
	b_count_list.append((b_artist_list[x] +' appears '+ str(b_artist_list.count(b_artist_list[x])) +' times on the Billboard Charts'))
	x = x + 1

b_final_count_list = list(set(b_count_list))
b_new_count_list = sorted(b_final_count_list, reverse=False)
print(*b_new_count_list, sep='\n')

#timer for billboard code 
b_now = time.time()

print('Done creating Billboard Music List ... Took '+ str(b_now-b_then) + ' seconds')
print('------------------------------------------------------------------------')

#timer for spotify code 
s_then = time.time()

#all spotify artist names
s_all_artist = List['spotify'].find_all('span')
s_intial_artist_list = []
s_update_artist_list = []

#putting spotify artist in a list 
for artist in s_all_artist:
	s_intial_artist_list.append(artist.text.strip())

#removing "by" before spotify artist name
for new_artist in s_intial_artist_list:
	x = new_artist[2:].strip()
	s_update_artist_list.append(x)
	

#all spotfiy song names
s_all_song = List['spotify'].find_all('strong')
s_song_list = []

#putting spotify song in a list 
for song in s_all_song:
 	s_song_list.append(song.text.strip())

#all spotify stream numbers
s_all_streams = List['spotify'].find_all(class_='chart-table-streams')
s_streams_list = []

#putting spotify streams in a list 
for streams in s_all_streams:
 	s_streams_list.append(streams.text.strip())

#putting artist and song into csv file 
i=0
while i < len(s_all_song):
	s_csv_writer.writerow([i+1,s_update_artist_list[i],s_song_list[i],s_streams_list[i+1]])
	i = i + 1

#counting number of times artist appears on list
x=0
s_count_list = []
while x < len(s_update_artist_list):
	s_count_list.append((s_update_artist_list[x] +' appears '+ str(s_update_artist_list.count(s_update_artist_list[x])) +' times on the Spotity Charts'))
	x = x + 1

s_final_count_list = list(set(s_count_list))
s_new_count_list = sorted(s_final_count_list, reverse=False)
print(*s_new_count_list, sep='\n')

#timer for spotify code 
s_now = time.time()

print('Done creating Spotity List ... Took '+ str(s_now-s_then) + ' seconds')
print('------------------------------------------------------------------------')

now = time.time()

print('Done:'+ str(now-then) + ' seconds')



