#from flask import Flask, json, session, jsonify
from datetime import datetime
from datetime import timedelta
#from .db_models import User, Tag, Twitch_URL
#from run import db
#import db_models 
import twitch_api

get_latest_ts = "SELECT date FROM Twitch_URL WHERE game_name = '%s' ORDER BY date DESC LIMIT 1"
get_urls_from_Twitch_Url_db = "SELECT * FROM Twitch_URL WHERE game_name = '%s' ORDER BY date LIMIT 30"
get_game_names_from_Tag_db = "SELECT tags FROM Tag WHERE user_id = %s LIMIT 1"
insert_Twitch_URL = "INSERT INTO Twitch_URL(url, date, tag_id, game_name) VALUES (%s,%s,%s,%s)"

def get_clips(database_inst, user_id, tags, date_comp): #user_id: int, tags: string
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
	#dates = []
	#thumbnail_urls = []
	#games = []

	tags_list = tags.split(',')
	print("TAGS_LIST: " + str(tags_list)) 
	for game in tags_list:
		print("GAME: " + str(game))
		date_db_query = get_latest_ts % game
		print("DATE DB QUERY: " + str(date_db_query))
		#date_db_result = database_inst.query(date_db_query)
		
		#date_comp = (now - date_db_result).total_seconds()
		#date_comp = 1400
		if int(date_comp) < 1500 or date_comp == None: 
			#if less than 5 min from most recent timestamp and current timestamp or no entries
			#exist in DB, pull from DB
			get_url_from_Twitch_Url_db_query = get_urls_from_Twitch_Url_db % (game)
			print("GET URL FROM DB: " + get_url_from_Twitch_Url_db_query)

			''' NEED TO BE TESTED
			result = database_inst.query(get_url_from_Twitch_Url_db_query) 
			for row in result:
				urls.append(row[1])
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
				#print("ID :" + str(entry_id) + ", TS: " + str(entry_ts) + ", URL: " + str(entry_url) + " THUMBNAIL: " + str(entry_thumbnail_url))
				urls.append(entry_embed_url)
				#dates.append(entry_ts)
				#thumbnail_urls.append(entry_thumbnail_url)
				#games.append(game)

				insert_query = insert_Twitch_URL % (entry_embed_url, entry_ts, entry_game_id, game)
				#print((entry_embed_url, entry_ts, entry_game_id, game))
				#print("INSERT QUERY: " + str(insert_query))
				#database_inst.insert("Twitch_URL", (entry_embed_url, entry_ts, entry_game_id, game))

	if not urls: 
		print("ERROR: NO DATA FOUND\n")
		return {"data": "None"}, 404
	#print("URLS: " + str(urls))
	return urls #, games, dates

def recommend(email):
	"Return recommended clips based off of user categories from db"
	return "https://clips.twitch.tv/embed?clip=StylishAmericanPepperoniPJSugar-73riKqxnVTKoGsxI, https://clips.twitch.tv/embed?clip=StormyTentativeGooseNerfBlueBlaster-fz6AoxMLgYa1bK4K, https://clips.twitch.tv/embed?clip=SleepyConsiderateCurryRuleFive-YxNspoxXoNAqxhCA"

if __name__ == "__main__":
	print("__________________________")
	print("QUERY FROM DB TEST: \n")
	get_clips("db", "1234", "VALORANT,League of Legends" , 1400)
	print("__________________________")
	print("QUERY FROM TWITCH API TEST: \n")
	get_clips("db", "1234", "VALORANT,League of Legends" , 1600)

