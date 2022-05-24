import sqlite3
from os import path
from werkzeug.security import generate_password_hash, check_password_hash

DB_NAME = 'database.db'
class database():
    def __init__(self):
        #self.connection = sqllite3.connect('database.db')
        if not path.exists('BE/' + DB_NAME):
            self.connection = sqlite3.connect('database.db')
            with open('schema.sql') as f:
                self.connection.executescript(f.read()) #create tables
        else:
            self.connection = sqlite3.connect('database.db')
    '''
        def insert(self, tablename,data):
            try:
                cur = self.connection.cursor()
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
    '''
    def query(self, query):
        try:
            cur = self.connection.cursor()
            results = cur.execute(query)
            return results
        except Exception as e:
            return(str(e))
        
    #def all_tags(self):
        #pass """

    def generateNewToken(self, email):
        """ Generate new token for user with email """
        return True

    def checkIfValidUser(self, email, token):
        """ Check if user is valid with specific token. Return true or false """
        sql = "SELECT * FROM User WHERE email = '%s' and token = '%s' LIMIT 1"
        get_login_info = sql % (email, token)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info) #should return the login info from DB
        if data:
            return True
        else:
            return False


    def checkIfValidUserPass(self,email, password):
        """ If User is valid return a generated token
        If not return False """

        password1 = generate_password_hash(password, method = 'sha256')
        sql = "SELECT * FROM User WHERE email = '%s' and password1 = '%s' LIMIT 1"
        get_login_info = sql % (email, password1)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info) #should return the login info from DB
        if not data:
            return False
        else:
            for row in data:
                return row[4]
        
        
        #return True

    def createNewUser(self, email, password, name):
        """ 
            If user doesn't exist in DB, create new user, insert into DB, return token
            If user already exists in DB, return false
        """
        password1 = generate_password_hash(password, method = 'sha256')
        sql = "SELECT * FROM User WHERE email = '%s' and password = '%s' and firstname = '%s' LIMIT 1"
        insert_sql = "INSERT INTO User(email, password1, firstname, token, tags) VALUES (%s,%s,%s,%s)"
        get_login_info = sql % (email, password1, name)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info) #should return the login info from DB
        if not data:
            #password1= generate_password_hash(password, method = 'sha256')
            token1= str(password1) + str(email) #passwordtest@gmail.com
            insert_sql_query = insert_sql % (email, password1, name, token1, "")
            print(insert_sql_query)
            data = self.query(insert_sql_query)
            for row in data:
                return row[4]
        else:
            return False
            

        #return True

    def getUserCategories(self, email):
        "Return a list of user selected categories"
        sql = "SELECT * FROM User WHERE email = '%s' LIMIT 1"
        get_login_info = sql % (email)
        print("GET LOGIN INFO: " + get_login_info)
        data = self.query(get_login_info)
        print("DATA: " + str(data))
        #data = [[1, 'test@gmail.com', 'test_password', 'VALORANT,APEX LEGENDS']]
        for row in data:
            return row[3]

        #return ["Valorant", "CSGO", "Apex Legends", "League of Legends"]

    def getAllCategories(self):
        "Return a list of all categories"
        categories = []
        sql = "SELECT DISTINCT tag FROM Twitch_URL"
        print("SQL: " + str(sql))
        data = self.query(sql)
        #data = [[1, 'VALORANT', 'www.twitch.tv...', '2022-05-22T20:53:31Z'],[2, 'APEX LEGENDS', 'www.twitch.tv...', '2022-05-22T20:53:31Z']]
        for row in data:
            categories.append(row[1])
        return categories
        #return ["Valorant", "CSGO", "League of Legends", "Minecraft", "Apex Legends", "Call of Duty WarZone", "Among Us", "Dota 2", "World of Warcraft" ]


    def setUserCategories(self, categories, email):
        #categories: single string | Ex: "VALORANT,APEX LEGENDS"
        "Takes categories and insert them into specific user cell"
        #categories = 
        sql = "UPDATE User SET tags = '%s' WHERE email = '%s'"
        sql_query = sql % (categories,email)
        print("SQL: " + str(sql_query))
        self.query(sql_query)
        return
        #return True

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
    createUser = database.createNewUser("test@gmail.com", "test_password", "testname")
    print(createUser)
    print("__________________________________")
    print("getUserCategories TEST")
    user_categories = database.getUserCategories("test@gmail.com")
    print(user_categories)
    print("__________________________________")
    print("getAllCategories TEST")
    categories = database.getAllCategories()
    print(categories)
    print("__________________________________")
    print("setUserCategories TEST")
    database.setUserCategories("VALORANT,APEX LEGENDS", "test@gamil.com")
    print("__________________________________")
