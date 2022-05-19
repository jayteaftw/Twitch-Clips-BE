from flask import Flask, json, session, jsonify
from flaskext.mysql import MySQL
from datetime import datetime
from datetime import timedelta
import twitch_api

#twitch API
GET_TAGS_FOR_SPECIFIC_CHANNEL = "curl -X GET 'https://api.twitch.tv/helix/streams/tags?bradcaster_id={} -H 'Authorization: Bearer {}' -H 'Client-Id: {}"

#based on clip ID, broadcaster_id, or game ID
GET_CLIPS = "curl -X GET 'https://api.twitch.tv/helix/clips?id={}' -H 'Authorization: Bearer {}' -H 'Client-Id: {}'"

#get first page of stream tags that Twitch defines
GET_ALL_TAGS = "curl -X GET 'https://api.twitch.tv/helix/tags/streams' -H 'Authorization: Bearer {}' -H 'Client-Id: {}'"


#name of database fields will change based on implementation  
'''
Login Table: Username, password
Users Liked Categories Table: UserId, GameName, GameId
Data Table: GameId, Url, Timestamp, NumViews
'''

#@app.route('/getClips/<tag1>/<tag2>/<tag3>/<tag4>/<tag5>')
def get_clips(user_id, game_name):
	twitch_api = twitch_api()
	now = datetime.now()
	time_start = twich_api.convert_time_RC3339(now.year, now.month, now.day, now.hour, now.minute, now.second) 	
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




