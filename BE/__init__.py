from pickle import NONE
from query_api import query_API
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from lib import load_flask_variables
from auth_api import api_blueprint
from flask_cors import CORS


def create_api():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    CORS(app)
    api = Api(app)

    env_variables = load_flask_variables()

    if env_variables is None: 
        print(f'"env_variables.json" was not found. First run? ') 
        print(f'"env_variables.json" has been created but some variables need to be changed.')
        print(f'Change the incorrect variables before relaunching!')
        exit()

    IP = env_variables["ip"]
    PORT = env_variables["port"]
    
    return app, IP, PORT




if __name__ == "__main__":
    app, IP, PORT = create_api()
    app.run(debug=True, host=IP, port=PORT)
