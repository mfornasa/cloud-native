from app import app, mongo, logger
from flask import request, render_template

# Importing the required objects from the Prometheus lib
from prometheus_client import Counter, Histogram, Gauge, Summary
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Adding a custom metric: let's count all Mongo insertions
object_counter = Counter('added_objects', 'Call to Mongo to add objects')

@app.route('/')
@app.route('/index')
def index():
  logger.info("Hello from Flask!")
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
    object_counter.inc()

    return 'created new thing named ' + name

@app.route("/metrics", methods=["GET"])
def metrics():
  headers = {'Content-Type': CONTENT_TYPE_LATEST}
  return generate_latest(), 200, headers
