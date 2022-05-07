import json

def load_env_variables(path= "env_variables.json"):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        
        data = {
                    "ip":"0.0.0.0",
                    "port":80,
                    "client_ID": "None",
                    "client_secret":"None",
                    }
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        
        return None