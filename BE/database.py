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
        sql = "SELECT * FROM User WHERE email = '%s' LIMIT 1"
        get_login_info = sql % (email)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info) #should return the login info from DB
        if data:
            return True
        else:
            return False

        return True

    def checkIfValidUserPass(self,email, password):
        """ If User is valid return a generated token
        If not return False """
        sql = "SELECT * FROM User WHERE email = '%s' and password = '%s' LIMIT 1"
        get_login_info = sql % (email, password)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info) #should return the login info from DB
        if not data:
            return False
        else:
            for row in data:
                return row[4]
        
        
        #return True

    def createNewUser(self, email, password): #, name):
        """ If User is created, return generated token
        If User is not created, return False """
        sql = "SELECT * FROM User WHERE email = '%s' and password = '%s' LIMIT 1"
        get_login_info = sql % (email, password)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info) #should return the login info from DB
        if not data:
            return False
        else:
            for row in data:
                return row[4]

        #return True

    def getUserCategories(self, email):
        "Return a list of user selected categories"
        sql = "SELECT * FROM User WHERE email = '%s' LIMIT 1"
        get_login_info = sql % (email)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info)
        data = [[1, 'test@gmail.com', 'test_password', 'VALORANT,APEX LEGENDS']]
        for row in data:
            return row[3]

        #return ["Valorant", "CSGO", "Apex Legends", "League of Legends"]

    def getAllCategories(self):
        "Return a list of all categories"
        
        return ["Valorant", "CSGO", "League of Legends", "Minecraft", "Apex Legends", "Call of Duty WarZone", "Among Us", "Dota 2", "World of Warcraft" ]


    def setUserCategories(self, categories, email):
        "Takes categories and insert them into specific user cell"
        return True

if __name__ == "__main__":
    database = database()
    print("__________________________________")
    print("checkIfValidUser TEST")
    IsValidUser = database.checkIfValidUser("test@gmail.com", "test_token")
    print(IsValidUser)
    print("__________________________________")
    print("checkIfValidUserPass TEST")
    IsValidUserPass = database.checkIfValidUserPass("test@gmail.com", "test_password")
    print(IsValidUserPass)
    print("__________________________________")
    print("createNewUser TEST")
    createUser = database.createNewUser("test@gmail.com", "test_password")
    print(createUser)
    print("__________________________________")
    print("getUserCategories TEST")
    user_categories = database.getUserCategories("test@gmail.com")
    print(user_categories)
    print("__________________________________")
