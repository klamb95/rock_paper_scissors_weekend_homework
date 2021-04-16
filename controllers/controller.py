from flask import render_template, request, redirect
from app import app
from models.player import *
from models.game import players, get_preferred_option, get_this_working, this_works

@app.route('/<choice_1>/<choice_2>')
def index(choice_1, choice_2):
    winner = this_works(choice_1,choice_2)
    return render_template('index.html', winner = winner)


#below works!
# @app.route("/<choice_1>/<choice_2>")
# def index(choice_1, choice_2):
#     winner = this_works(choice_1,choice_2)
#     return render_template('index.html', winner = winner)