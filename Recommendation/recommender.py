from flaskext.myql import MySQL
#may need to change DB based on what we need

@app.route('/getClips/<tag1>/<tag2>/<tag3>/<tag4>/<tag5>')
def get_clips(tag1,tag2,tag3,tag4,tag5):
	try:
		if session.get('user'):
			_id = request.form['id']
			_user = session.get('user')
			conn = msql.connect()
			cursor = conn.cursor()
			cursor.callproc('getClipsFromDB', (_id,_user,tag1,tag2,tag3,tag4,tag5)) #need to write SQL query to grab based in id, user, tags
			result = cursor.fetchall()
			clips = []
			clips.append() #need to add based on what we have in DB
			if not clips:
				pass
				#need to query from twitch API
			else:
				return json.dumps(clips)
	except Exceptions as e:
		return render_template('error.html', error = 'Bad Request')



