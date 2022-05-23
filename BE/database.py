from lib2to3.pgen2 import token


class database():
  
    """ cur = db.cursor() """
    def __init__(self):
        pass
        # maybe add DB creation and Tables creation part here
        

    def insert(self, tablename,data):
        pass
        """ try:
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
            return(str(e)) """

    def query(self, query):
        pass
        """ try:
            res = cur.execute(query)
            return res
        except Exception as e:
            return(str(e))
        
    #def all_tags(self):
        #pass """

    def generateNewToken(self, email):
        """ Generate new token for user with email """
        return True

    def checkIfValidUser(self, email, token):
        """ Check if user is valid with specific token. Return true or false """
        return True

    def checkIfValidUserPass(self,email, password):
        """ If User is valid return a generated token
        If not return False """
        
        return True

    def createNewUser(self, email, password, name):
        """ If User is created, return generated token
        If User is not created, return False """

        return True

    def getUserCategories(self, email):
        "Return a list of user selected categories"

        return ["Valorant", "CSGO", "Apex Legends", "League of Legends"]

    def getAllCategories(self):
        "Return a list of all categories"

        return ["Valorant", "CSGO", "League of Legends", "Minecraft", "Apex Legends", "Call of Duty WarZone", "Among Us", "Dota 2", "World of Warcraft" ]


    def setUserCategories(self, categories, email):
        "Takes categories and insert them into specific user cell"
        return True