import requests
import datetime
from lib import load_twitch_variables


class twitch_api():
    CLIENT_ID = None
    BEARER_TOKEN = None

    def __init__(self, path="variables/twitch_variables.json"):
        variables = load_twitch_variables(path)
        self.CLIENT_ID = variables["client_ID"]
        self.BEARER_TOKEN = variables["token"]


    def get_game_ID(self, game_name):
        message = requests.get( url=f"https://api.twitch.tv/helix/games?name={game_name}", 
                            headers={   "Authorization":"Bearer "+self.BEARER_TOKEN,
                                        "client-Id": self.CLIENT_ID
                                    })
        return message.json()['data'][0]["id"]


    def get_game_clips(self, game_ID, time, clip_count=100):
        message = requests.get( url=f'https://api.twitch.tv/helix/clips?game_id={game_id}&started_at=2022-05-10T00:00:00Z&first=50', 
                            headers={   "Authorization":"Bearer "+self.BEARER_TOKEN,
                                        "client-Id": self.CLIENT_ID,
                                    })
        return message

    def convert_time_RC3339(self,year, month, day, hour, minutes, seconds):
        return f'{year}-{month}-{day}T{hour}:{minutes}:{seconds}Z'


if __name__ == "__main__":
    


    twitch_api = twitch_api()

    time = twitch_api.convert_time_RC3339(2020,5,11,00,00,00)

    game_id = twitch_api.get_game_ID("VALORANT")

    message = twitch_api.get_game_clips(game_id, None, time)

    print(message.json())

    b = datetime.datetime(2021,1,1)

    for i in message.json()['data']:
        if datetime.datetime.strptime(i["created_at"], '%Y-%m-%dT%H:%M:%SZ') > b:
            print(i['id'], "\t", i["created_at"], i["url"], i["language"] )

    print(message.json()['data'][0])

    time  = message.json()['data'][0]['created_at']
    x = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    print(x.time)