
from __init__ import db
class database():
    cur = db.cursor()
    def __init__(self):
        # maybe add DB creation and Tables creation part here
        

    def insert(self, tablename,data):

        try:
            if tablename == User:
                sql =  "INSERT INTO User ( email , name , password ) VALUES (%s,%s,%s)"
            elif tablename == Tag:
                sql =  "INSERT INTO Tag ( tags , user_id ) VALUES (%s,%s)"
            else:
                sql =  "INSERT INTO Twitch_URL ( URL,date,tag_id) VALUES (%s,%s,%s)"

            val = data
            cur.execute(sql,val)
            db.session.commit()
            print ("Insert successfull")
        except Exception as e:
            return(str(e))

    def query(self, querry):
        try:
            res = cur.execute(querry)
            return res
        except Exception as e:
            return(str(e))
        
    #def all_tags(self):
        #pass
    