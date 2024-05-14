import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Bird

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://maomau:fS1CAy1ydvlu07VpwSz80YZVKpgMIryL@dpg-cp1p30ed3nmc73b8vv1g-a.virginia-postgres.render.com/bird_app_vo78"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)
    
api.add_resource(Birds, '/birds')