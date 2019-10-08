from bs4 import BeautifulSoup
import requests
import csv
import time
import random

then = time.time()

#creating csv file for spotify list

s_csv_file = open('Spotify.csv','w')
s_csv_writer = csv.writer(s_csv_file)
s_csv_writer.writerow(['Rank','Artist','Song','Streams'])

#Spotify url link 
s_link = 'https://spotifycharts.com/regional/us/daily/latest'

#query the Spotify website and return the html 
s_page = requests.get(s_link).text

#convert Spotify website to beautifulSoup
s_soup = BeautifulSoup(s_page, 'html.parser')


#spotify music list 
s_list = s_soup.find(class_='chart-table')

#all spotify artist names
s_all_artist = s_list.find_all('span')
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
s_all_song = s_list.find_all('strong')
s_song_list = []

#putting spotify song in a list 
for song in s_all_song:
 	s_song_list.append(song.text.strip())

#all spotify stream numbers
s_all_streams = s_list.find_all(class_='chart-table-streams')
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

now = time.time()

print('Done creating Spotity List ... Took '+ str(now-then) + ' seconds')



