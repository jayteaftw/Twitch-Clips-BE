import requests
from datetime import datetime, timedelta
from lib import load_twitch_variables, upload_refresh_token


class twitch_api():
    CLIENT_ID = None
    BEARER_TOKEN = None

    def __init__(self, path="variables/twitch_variables.json"):
        variables = load_twitch_variables(path)

        if(variables == None):
            print(f'"twitch_variables.json" was not found. First run? ') 
            print(f'"twitch_variables.json" has been created but some variables need to be changed.')
            print(f'Change the incorrect variables before relaunching!')
            exit()

        self.CLIENT_SECRET = variables["client_secret"] 
        self.CLIENT_ID = variables["client_ID"]
        self.BEARER_TOKEN = variables["token"]
        
        print(variables)
        if self.BEARER_TOKEN == None:
            self.token_refresh()
            variables = load_twitch_variables(path)
        
        self.EXPIRATION_DATE = variables["expiration_date"]

        expiration_date = datetime.fromisoformat(self.EXPIRATION_DATE)
        if expiration_date- timedelta(days=1) < datetime.now() :
            self.token_refresh()

        if(self.CLIENT_ID == None or self.CLIENT_SECRET == None):
            print(f"ERROR!!! Client Secret({self.CLIENT_SECRET}) or ID({self.CLIENT_ID}) is Missing???")
            exit()


    def get_game_ID(self, game_name):
        message = requests.get( url=f"https://api.twitch.tv/helix/games?name={game_name}", 
                            headers={   "Authorization":"Bearer "+self.BEARER_TOKEN,
                                        "client-Id": self.CLIENT_ID
                                    })
        return message.json()['data'][0]["id"]

    def get_user_ID(self, user_name):
        message = requests.get( url=f"https://api.twitch.tv/helix/users?login={user_name}", 
                            headers={   "Authorization":"Bearer "+self.BEARER_TOKEN,
                                        "client-Id": self.CLIENT_ID
                                    })
        return message.json()['data'][0]["id"]

    def get_game_clips(self, game_ID, time_start, time_end=None, clip_count=100, cursor=None):

        url = f'https://api.twitch.tv/helix/clips?game_id={game_ID}&started_at={time_start}&first={clip_count}'\
                + ("" if not time_end else f"&ended_at={time_end}") \
                + ("" if not cursor else f"&after={cursor}")
                
        message = requests.get( url=url, 
                                headers={   "Authorization":"Bearer "+self.BEARER_TOKEN,
                                            "client-Id": self.CLIENT_ID
                                        })
        return message
    
    def get_user_clips(self, user_ID, time_start, time_end=None, clip_count=100, return_limit=False, cursor=None):
        url = f'https://api.twitch.tv/helix/clips?broadcaster_id={user_ID}&started_at={time_start}&first={clip_count}' \
                + ("" if not time_end else f"&ended_at={time_end}") \
                + ("" if not cursor else f"&after={cursor}")

        message = requests.get( url=url, 
                                headers={   "Authorization":"Bearer "+self.BEARER_TOKEN,
                                            "client-Id": self.CLIENT_ID
                                        })
        return message

    def convert_time_RC3339(self,year, month, day, hour, minutes, seconds):
        f = lambda x: str(x).zfill(2)
        return f'{f(year)}-{f(month)}-{f(day)}T{f(hour)}:{f(minutes)}:{f(seconds)}Z'

    def token_refresh(self):
        url =   f"https://id.twitch.tv/oauth2/token?client_id={self.CLIENT_ID}" + \
                f"&client_secret={self.CLIENT_SECRET}&grant_type=client_credentials"
        message = requests.post(url=url)

        creation_date = datetime.now()
        print(message.json())
        self.BEARER_TOKEN = message.json()['access_token']
        upload_refresh_token(self.BEARER_TOKEN, creation_date, message.json()['expires_in'])

if __name__ == "__main__":

    twitch_api = twitch_api()

    broadcast_ID = twitch_api.get_user_ID("tarik")

    time_start = twitch_api.convert_time_RC3339(2022,5,9,"0","0","0")

    time_ended = twitch_api.convert_time_RC3339(2022,5,9,"2","0","0")

    game_id = twitch_api.get_game_ID("VALORANT")

    #message = twitch_api.get_user_clips(broadcast_ID, time_start, time_ended)
    message = twitch_api.get_game_clips(game_id, time_start, time_ended)

    print(message.json())

    b = datetime(2021,1,1)

    for i in message.json()['data']:
        if datetime.strptime(i["created_at"], '%Y-%m-%dT%H:%M:%SZ') > b:
            print(i['id'], "\t", i["created_at"], i["embed_url"], i["language"] )

    print(message.json()['data'][0])

    time  = message.json()['data'][0]['created_at']
    x = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    print(x.time)

    exit()
    count = 0
    cursor = None
    while count < 5:
        message = twitch_api.get_user_clips(broadcast_ID, time_start, time_ended, cursor=cursor).json()
        data = message['data']
        #print(data)
        cursor = message['pagination']['cursor']
        print(cursor)
        if cursor == None: break
        count += 1