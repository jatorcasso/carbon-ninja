from flask import Flask
from flask_restful import Resource, Api
from .predict import Predict
from .foods import Foods

application = Flask(__name__)
api = Api(application)

@application.route('/', methods=['GET'])
def home():
    return "Call for Code"

api.add_resource(Predict, '/predict')
api.add_resource(Foods, '/foods')
