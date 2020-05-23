from bs4 import BeautifulSoup
import requests
import csv
import time
import random
import psycopg2
from pymongo import MongoClient
import dns
import pandas as pd
import json
#import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode
import pandas


then = time.time()
#creating csv file for Apple Music List
a_csv_file = open('csv/AppleMusic.csv','w')
a_csv_writer = csv.writer(a_csv_file)
a_csv_writer.writerow(['Rank','Artist','Song'])

#creating csv file for Billboard List
b_csv_file = open('csv/BillboardTop100.csv','w')
b_csv_writer = csv.writer(b_csv_file)
b_csv_writer.writerow(['Rank','Artist','Song'])

#creating csv file for Spotify List
s_csv_file = open('csv/Spotify.csv','w')
s_csv_writer = csv.writer(s_csv_file)
s_csv_writer.writerow(['Rank','Artist','Song','Streams'])


#url link for apple music,billboard,spotify

link = {
	'applemusic': ('https://kworb.net/charts/apple_s/us.html'),
	'billboard' : ('https://www.billboard.com/charts/hot-100'),
	'spotify': ('https://spotifycharts.com/regional/us/daily/latest'), 
}

#query the apple music,billboard & spotify website and return the html 
page = {
	'applemusic': (requests.get(link['applemusic']).text),
	'billboard' : (requests.get(link['billboard']).text),
	'spotify': (requests.get(link['spotify']).text),
}


#convert apple music,billboard,spotify website to beautifulSoup
soup = {
	'applemusic': (BeautifulSoup(page['applemusic'], 'html.parser')),
	'billboard': (BeautifulSoup(page['billboard'], 'html.parser')),
	'spotify': (BeautifulSoup(page['spotify'], 'html.parser')),
}

#apple music,billboard,spotify list 
List = {
	'applemusic': (soup['applemusic'].find('tbody')),
	'billboard': (soup['billboard'].find(class_='chart-list__elements')),
	'spotify': (soup['spotify'].find(class_='chart-table')),
} 

#timer for apple music code 
a_then = time.time()

#all apple music artist names
a_all_artist = List['applemusic'].find_all(class_='mp text')
a_artist_list = []

#putting apple music artist in a list 
for artist in a_all_artist:
	temp = artist.text.split(' - ')
	a_artist_list.append(temp[0].strip().upper())

#all apple music song names
a_all_song = List['applemusic'].find_all(class_='mp text')
a_song_list = []

#putting apple music song in a list 
for song in a_all_song:
	temp = song.text.split(' - ')
	a_song_list.append(temp[1].strip().title())

#putting apple music artist and song into csv file 
i=0
while i < len(a_artist_list):
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
	b_artist_list.append(artist.text.strip().upper())

#putting billboard song in a list 
for song in b_all_song:
	b_song_list.append(song.text.strip().title())

#putting billboard artist and song into csv file 
i=0
while i < 100:
	b_csv_writer.writerow([i+1,(b_artist_list[i]).strip(),(b_song_list[i]).strip()])
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
	s_update_artist_list.append(x.upper())
	

#all spotfiy song names
s_all_song = List['spotify'].find_all('strong')
s_song_list = []

#putting spotify song in a list 
for song in s_all_song:
 	s_song_list.append(song.text.strip().title())

#all spotify stream numbers
s_all_streams = List['spotify'].find_all(class_='chart-table-streams')
s_streams_list = []

#putting spotify streams in a list 
for streams in s_all_streams:
 	s_streams_list.append(streams.text.strip().replace(',', ''))

#putting artist and song into csv file 
i=0
while i < len(s_all_song):
	s_csv_writer.writerow([i+1,(s_update_artist_list[i]).strip(),(s_song_list[i]).strip(),s_streams_list[i+1]])
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


print('--------------------')

#creating csv file for all artist
ma_csv_file = open('csv/MasterArtist.csv','w')
ma_csv_writer = csv.writer(ma_csv_file)
ma_csv_writer.writerow(['id','Artist'])

#creating csv file for all songs
ms_csv_file = open('csv/MasterSong.csv','w')
ms_csv_writer = csv.writer(ms_csv_file)
ms_csv_writer.writerow(['id','Song'])


#master_song_list = 
master_artist_list = a_artist_list + b_artist_list + s_update_artist_list
master_song_list = a_song_list + b_song_list + s_song_list
master_song_list = list(dict.fromkeys(master_song_list))
master_artist_list = list(dict.fromkeys(master_artist_list))
master_artist_list = sorted(master_artist_list,reverse=False)
master_song_list = sorted(master_song_list)

#putting artist and song into csv file 
i=0
while i < len(master_artist_list):
	ma_csv_writer.writerow([i+1,master_artist_list[i]])
	i = i + 1

#putting artist and song into csv file 
i=0
while i < len(master_song_list):
	ms_csv_writer.writerow([i+1,master_song_list[i]])
	i = i + 1

def applemusic_stuff():
	link = 'https://itunes.apple.com/search?term=young+thug&entity=musicTrack'

	make_json = requests.get(link).json()



	print(json.dumps(make_json, indent=3))

def pg_load_table(file_path,table_name):

    SQL_STATEMENT = """
    COPY %s FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS ','
    """

    try:
        conn = psycopg2.connect(host='127.0.0.1',port='5432',database='music',user='udk',password='Nigerian24')
        print("Connecting to Database")
        cur = conn.cursor()
        f = open(file_path, "r")
        #truncate aka clear it before loading it
        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        cur.copy_expert("copy {} from STDIN CSV HEADER DELIMITER AS ',' ".format(table_name), f)
        # Load table from the file with header
        #cur.copy_from(f,str(table_name))
        conn.commit()
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))

#path,table
#client = pymongo.MongoClient("mongodb+srv://ued2:Nigerian24@music-fcmml.mongodb.net/test?retryWrites=true&w=majority")
def mysql():
	try:
		cnx = connection.MySQLConnection(user='root', password='Nigerian24',
                              host='127.0.0.1',
                              database='musicstats')

		cursor = cnx.cursor()

		print(cnx)

		#mysql.connector.connection_cext.CMySQLConnection object at 0x110e50ed0

		print(cursor)

		#CMySQLCursor: (Nothing executed yet)

		cursor.execute("show tables")

		for x in cursor:
			print(x)


		""""

		cur = cnx.cursor()

		csv_data = pandas.read_csv(path)

		#csv_data = csv.reader(file(path), delimeter=',')

		count = 0 

		db = mysql.connector.connect(user='root', password='Nigerian24',host='127.0.0.1')

		for row in csv_data:
			if count < 1:
				continue
			else:
				cur.execute("INSERT INTO {} (id,name) VALUES (%s, %s)".format(table), row)
				print(table + '--->'+ count)
			count +=1

		"""

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		cnx.commit()
		cnx.close()


#applemusic_stuff()


#mysql()
pg_load_table('/Users/udk/Desktop/musicstats/csv/MasterArtist.csv','artist')
pg_load_table('/Users/udk/Desktop/musicstats/csv/MasterSong.csv','song')
pg_load_table('/Users/udk/Desktop/musicstats/csv/AppleMusic.csv','applemusic')
pg_load_table('/Users/udk/Desktop/musicstats/csv/Spotify.csv','spotify')
pg_load_table('/Users/udk/Desktop/musicstats/csv/BillboardTop100.csv','billboard')



