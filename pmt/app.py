from flask import Flask
from flask_restful import Resource, Api
from .views.views import UserView
from .models.model import db
from . import configuration


class Hello(Resource):
    def get(self):
        return {'hello': 'I\'m andy'}


app = Flask(__name__, instance_relative_config=True)
logger = app.logger

api = Api(app)

api.add_resource(Hello, '/')
api.add_resource(UserView, '/user')

app.config.from_object(configuration.DevelopmentConfig)
db.init_app(app)

