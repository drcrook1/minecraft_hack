'''
Author: David Crook
Copyright: Microsoft Corporation 2018
'''
from flask import Flask
from pymongo import MongoClient
import ssl
import os


def resolve_mongo_conn_string():
    return os.environ["MONGO_CONN_STRING"]


def create_app():
    app = Flask(__name__)

    # Register BluePrints
    from app.views.views import views
    app.register_blueprint(views)

    from app.apis.kubernetes import kubernetes
    app.register_blueprint(kubernetes)

    #register_extensions(app)

    return app

# def register_extensions(app):
#     global db
#     db = MongoClient(resolve_mongo_conn_string()).kubernetes
