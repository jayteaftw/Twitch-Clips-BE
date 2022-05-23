#from flask import Flask, json, session, jsonify
from datetime import datetime
from datetime import timedelta
from database import database
#from .db_models import User, Tag, Twitch_URL
#from run import db
#import db_models 
import twitch_api
import random

get_latest_ts = "SELECT date FROM Twitch_URL WHERE tag = '%s' ORDER BY date DESC LIMIT 1"
get_urls_from_Twitch_Url_db = "SELECT * FROM Twitch_URL WHERE tag = '%s' ORDER BY date LIMIT 30"
get_game_names_from_Tag_db = "SELECT tags FROM User WHERE email = %s LIMIT 1"
insert_Twitch_URL = "INSERT INTO Twitch_URL(tag, url, date) VALUES (%s,%s,%s)"
db = database()

def get_clips(tags): #user_id: int, tags: string
	twitch_inst = twitch_api.twitch_api()
	now = datetime.now()
	
	'''Calculating time period '''
	#print("NOW: " + str(now))
	time_start_hour = int(now.hour) - 2
	time_start = twitch_inst.convert_time_RC3339(now.year, now.month, now.day, time_start_hour, now.minute, now.second) 	
	#print("TIME START: " + str(time_start))
	time_end = twitch_inst.convert_time_RC3339(now.year, now.month, now.day, now.hour, now.minute, now.second)
	#print("TIME END: " + str(time_end))
	
	urls = []
	tags_list = tags.split(',')
	print("TAGS_LIST: " + str(tags_list)) 
	for game in tags_list:
		print("GAME: " + str(game))
		date_db_query = get_latest_ts % game
		print("DATE DB QUERY: " + str(date_db_query))
		#date_db_result = db.query(date_db_query)
		
		#date_comp = (now - date_db_result).total_seconds()
		date_comp = 1600
		if int(date_comp) < 1500 or date_comp == None: 
			#if less than 5 min from most recent timestamp and current timestamp or no entries
			#exist in DB, pull from DB
			get_url_from_Twitch_Url_db_query = get_urls_from_Twitch_Url_db % (game)
			print("GET URL FROM DB: " + get_url_from_Twitch_Url_db_query)

			''' NEED TO BE TESTED
			result = db.query(get_url_from_Twitch_Url_db_query) 
			for row in result:
				urls.append(row[3])
			'''


		else:
			'''TWITCH API PART'''
			print("game IN ELSE:" + str(game))
			game_id = twitch_inst.get_game_ID(str(game)) #replaced with game_names
			print("GAME_ID: " + str(game_id))
			message = []
			message = twitch_inst.get_game_clips(int(game_id), time_start, time_end)
			#print(message.json()['data'][0])

			for entry in message.json()['data']:
				entry_id = entry['id']
				entry_ts = entry['created_at'] # string type
				entry_ts2 = datetime.strptime(entry_ts, '%Y-%m-%dT%H:%M:%SZ')
				entry_url = entry['url']
				#print("URL: " + str(entry_url))
				entry_embed_url = entry['embed_url']
				entry_thumbnail_url = entry['thumbnail_url']
				entry_game_id = entry['game_id']
				
				urls.append(entry_embed_url)

				insert_query = insert_Twitch_URL % (game, entry_embed_url, entry_ts)
				#print((game, entry_embed_url, entry_ts))
				#print("INSERT QUERY: " + str(insert_query))
				#db.insert("Twitch_URL", (game, entry_embed_url, entry_ts))

	#print("URLS: " + str(urls))
	return urls #, games, dates

def recommend(email):
	"Return recommended clips based off of user categories from db"
	
	get_tags_query = get_game_names_from_Tag_db % email
	print("GET TAGS QUERY: " + get_tags_query)
	#results = db.query(get_tags_query)
	results = [[1, 'test@gmail.com', 'test_password', 'VALORANT,APEX LEGENDS']]
	for row in results:
		print("Tags: " + str(row[3]))
		urls = get_clips(row[3])
		print("URLS: " + str(urls))
		if not urls:
			 print("NO DATA IN URLS")
			 return
		random.shuffle(urls)
		print("__________________________")
		print(urls)
		print("__________________________")
		return urls
	#return "https://clips.twitch.tv/embed?clip=StylishAmericanPepperoniPJSugar-73riKqxnVTKoGsxI, https://clips.twitch.tv/embed?clip=StormyTentativeGooseNerfBlueBlaster-fz6AoxMLgYa1bK4K, https://clips.twitch.tv/embed?clip=SleepyConsiderateCurryRuleFive-YxNspoxXoNAqxhCA"

if __name__ == "__main__":
	#print("__________________________")
	#print("QUERY FROM DB TEST: \n")
	#get_clips("db", "1234", "VALORANT,League of Legends" , 1400)
	#print("__________________________")
	#print("QUERY FROM TWITCH API TEST: \n")
	#get_clips("db", "1234", "VALORANT,League of Legends" , 1600)

	recommend("test@gmail.com")
