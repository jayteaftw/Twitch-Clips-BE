from flask import request, render_template
from flask_restful import Api, Resource, reqparse


query_get_args = reqparse.RequestParser()
query_get_args.add_argument("")


query_post_args = reqparse.RequestParser()
query_post_args.add_argument("tags", required=True)


class query_API(Resource):

    #Get a list of available broadcasters and game categories
    def get():
        return 200
    
    #Make a clip query
    def post(self):
        return {"message": "hello"}, 200#Recommendation System Call

    def delete():
        pass

    def patch():
        pass