"""
Author: David Crook
Copyright: Microsoft 2019
"""
from app.app import create_app
from pymongo import MongoClient
from flask import render_template

app = create_app()

app.run(host='0.0.0.0', port=80)
