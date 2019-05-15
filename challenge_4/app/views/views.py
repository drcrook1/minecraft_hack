from flask import render_template, url_for, Blueprint, redirect, flash, request, current_app, send_from_directory

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
def index():
    return render_template('index.html')