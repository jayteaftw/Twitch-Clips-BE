from flask import request, Blueprint
from flask_restful import reqparse
from recommender import recommend
from database import database

api_blueprint = Blueprint('api_blueprint', __name__)
db = database()


@api_blueprint.route('/signIn', methods=['GET', 'POST'])
def signIn():
    args = request.json
    print(args)
    res = db.checkIfValidUserPass(args["email"], args["password"])
    userCategories = ""
    allCategories = db.getAllCategories()
    if res:
        userCategories = db.getUserCategories(args["email"])
    return {"token": str(res), "checked": userCategories, "categories":allCategories}, 200


@api_blueprint.route('/signUp', methods=['GET', 'POST'])
def signUp():
    print(request)
    args = request.json
    res = db.createNewUser(args["email"], args["password"], args["name"])
    userCategories = ""
    allCategories = db.getAllCategories()
    return {"token": str(res), "checked": userCategories, "categories":allCategories}, 200


@api_blueprint.route('/selection', methods=['GET', 'POST'])
def selection():
    args = request.json
    data = ""
    print(args)
    print(args["categories"])
    if db.checkIfValidUser(args["email"], args["token"]):
        db.setUserCategories(args["categories"], ["email"])
        data = recommend(args["email"])
    print(data)
    return {"links":data}, 200

@api_blueprint.route('/query', methods=['GET', 'POST'])
def query():
    args = request.json
    print("links")
    data = ""
    if db.checkIfValidUser(args["email"], args["token"]):
        data = recommend(args["email"])
    data = "https://clips.twitch.tv/embed?clip=StylishAmericanPepperoniPJSugar-73riKqxnVTKoGsxI, https://clips.twitch.tv/embed?clip=StormyTentativeGooseNerfBlueBlaster-fz6AoxMLgYa1bK4K, https://clips.twitch.tv/embed?clip=SleepyConsiderateCurryRuleFive-YxNspoxXoNAqxhCA"
    return {"links":data}, 200


