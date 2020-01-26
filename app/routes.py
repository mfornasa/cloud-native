from app import app, mongo
from flask import request

@app.route('/')
@app.route('/index')
def index():
  return "Hello, World!"

@app.route('/thing/<name>', methods=["GET"])
def get_thing(name):
  thing = mongo.db.things.find_one({"_id": name})
  if thing is not None:
    return thing
  else: 
    return 'thing named ' + name + ' does not exist'

@app.route("/thing/<name>", methods=["POST"])
def create_thing(name):
  data = request.json
  thing = mongo.db.things.find_one({"_id": name})
  if thing is not None:
    return 'thing named ' + name + ' is already existing'
  else: 
    thing = mongo.db.things.insert_one(
      {
        "_id": name,
        "description": data['description'] or "no description"
      })
    return 'created new thing named ' + name
