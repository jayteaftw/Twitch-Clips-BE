from flask import request
from flask_restful import Api, Resource, reqparse
from database import database


query_get_args = reqparse.RequestParser()
query_get_args.add_argument("")


query_post_args = reqparse.RequestParser()
query_post_args.add_argument("tags", required=True)

db = database()

class query_API(Resource):

    #Get a list of available broadcasters and game categories
    def get():
        return 200, db.all_tags()
    
    #Make a clip query
    def post():
        return 200 #Recommendation System Call

    def delete():
        pass

    def patch():
        pass