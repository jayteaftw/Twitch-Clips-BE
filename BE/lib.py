import json
from datetime import timedelta

def load_flask_variables(path= "variables/flask_variables.json"):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        
        data = {
                    "ip":"0.0.0.0",
                    "port":80
                    }
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        
        return None

def load_twitch_variables(path= "variables/twitch_variables.json"):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        
        data = {
                    "client_ID":None,
                    "client_secret":None,
                    "token": None,
                    "expiration_date": None
                    }
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        
        return None

def upload_refresh_token(token, creation_date, expiration_time, path= "variables/twitch_variables.json"):
    with open(path, 'r') as f:
        data = json.load(f)

    data["token"] = token
    data["expiration_date"] = creation_date + timedelta(seconds=expiration_time)

    with open(path, 'w') as f:
        json.dump(data, f, indent=2, default=str)
