import json

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
                    "Time": None
                    }
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        
        return None