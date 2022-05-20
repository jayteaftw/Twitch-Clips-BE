#from flask import Flask, json, session, jsonify
from datetime import datetime
from datetime import timedelta
#from .db_models import User, Tag, Twitch_URL
#from run import db
#import db_models 

import twitch_api

def get_clips(user_id, tags): #user_id: int, tags: string
	twitch_inst = twitch_api.twitch_api()
	now = datetime.now()
	
	'''Calculating time period '''
	#print("NOW: " + str(now))
	time_start_hour = int(now.hour) - 2
	time_start = twitch_inst.convert_time_RC3339(now.year, now.month, now.day, time_start_hour, now.minute, now.second) 	
	print("TIME START: " + str(time_start))
	time_end = twitch_inst.convert_time_RC3339(now.year, now.month, now.day, now.hour, now.minute, now.second)
	print("TIME END: " + str(time_end))

	urls = []
	dates = []
	thumbnail_urls = []
	games = []

	#ex_tags = "VALORANT,League of Legends"
	#tags_list = tags.split(',')
	#tags_list = ex_tags.split(',')
	#print("TAGS_LIST: " + str(tags_list) + ", [0]: " + tags_list[0])

	#date_db_query = Twitch_URL.query.filter_By(game_name = tags_list[0]).order_by(date).first().with_enttites(Twitch_URL.date)
	#date_comp = (now - date_db_query).total_seconds()
	date_comp = 1600
	if date_comp < 5 * 300: #if less than 5 min from most recent timestamp and current timestamp, pull from DB
		'''
		for tag in tags_list:
			db_query = Twitch_URL.query.filter_By(game_name = tag).order_by(date).limit(10)
			for r_url, r_date, r_tag_id, r_game_name in db_query:
				urls.append(r_url)
				dates.append(r_date)
				games.append(r_game_name)
		return urls, games, dates
		'''

	else:
		'''TWITCH API PART'''
		'''grabbing game_names from DB'''
		#game_names = Tag.query.filter_by(id=user_id).first().with_entities(Tag.tags)
		#db_query = Twitch_URL.query.filter_by(tag_id = game_id) #NEED TO FINISH

		game_names_from_DB = "VALORANT,League of Legends" #replaced with str(game_names)
		game_names_list = game_names_from_DB.split(',')
		for game in game_names_list:
			print("GAME:" + str(game))
			game_id = twitch_inst.get_game_ID(str(game)) #replaced with game_names
			print("GAME_ID: " + str(game_id))
			message = []
			message = twitch_inst.get_game_clips(int(game_id), time_start, time_end)
			#print(message.json()['data'][0])

			for entry in message.json()['data']:
				entry_id = entry['id']
				entry_ts = entry['created_at'] # string type
				entry_url = entry['url']
				entry_thumbnail_url = entry['thumbnail_url']
				entry_game_id = entry['game_id']
				#print("ID :" + str(entry_id) + ", TS: " + str(entry_ts) + ", URL: " + str(entry_url) + " THUMBNAIL: " + str(entry_thumbnail_url))
				urls.append(entry_url)
				dates.append(entry_ts)
				thumbnail_urls.append(entry_thumbnail_url)
				games.append(game)

				'''adding urls from TWITCH API to database'''
				#twitch_url_entry = Twitch_URL(url = str(entry_url), date = entry_ts, tag_id = entry_game_id)
				'''OPTION2: store game_name also'''
				#twitch_url_entry = Twitch_URL(url = str(entry_url), date = entry_ts, tag_id = entry_game_id, game_name = game)
				#db.session.add(twitch_url_entry)
			#db.session.commit()
			
		#print(urls)
		#print(thumbnail_urls)
		#print(games)
		#print(dates)
		if not urls and not games and not dates:
			return "ERROR: bad connection with DB"
		return urls, games, dates

	'''
	try:
		if session.get('user'):
			_id = request.form['id']
			_user = session.get('user')
			conn = msql.connect()
			cursor = conn.cursor()
			cursor.callproc('getGameNameFromDB', (user_id)) #need to write SQL query to grab based in id, user, tags
			profiles = cursor.fetchall()

			profiles_dict = []			
			for profile in profiles:
				profile_dict = {
					'UserId': profile[0],
					'GameName': profile[1],
					'GameId': profile[2]}
				profiles_dict.append(profile_dict)
			
			_game_name = profiles_dict[0]["GameName"]
			_game_id = profiles_dict[0]["GameId"]
			
			con2 = mysql.connect()
			cursor2 = con2.cursor()
			cursor2.callproc('getGameClips',(_game_name,_game_id))
			clips = cursor2.fetchall()

			if len(clips) == 0: #query from twitch api
				api_game_id = twitch_api.get_game_ID(str(game_name))
				api_clips = twitch_api.get_game_clips(api_game_id, time_start)
				return(api_clips)
			else: #convert request from DB to json format
				clips_dict = []
				for clip in clips:
					clips2  = {
						'GameId': clip[0],
						'Url': clip[1],
						'Timestamp': clip[2],
						'NumViews': clip[3]}
					clips_dict.append(clips2)
				return json.dumps(clips_dict)
	except Exceptions as e:
		print("Bad Request to DB")
		return
		#return render_template('error.html', error = 'Bad Request')
	'''

if __name__ == "__main__":
	get_clips("1234", "test")

