from flask import Flask, render_template, request, redirect, Blueprint

from models.park import Park
from repositories import park_repository
from repositories import land_repository
from repositories import attraction_repository

parks_blueprint = Blueprint("parks", __name__)

@parks_blueprint.route("/")
def parks():
    parks = park_repository.select_all()
    lands = land_repository.select_all()
    return render_template("/lands/index.html", parks = parks, lands = lands)

#NEW
@parks_blueprint.route("/parks/new", methods=['GET'])
def new_park():
    parks = park_repository.select_all()
    return render_template("parks/new.html", parks = parks)

#CREATE
@parks_blueprint.route("/parks", methods=['POST'])
def create_park():
    name = request.form['name']
    park = Park(name)
    park_repository.save(park)
    return redirect('/lands')

#SHOW
@parks_blueprint.route("/parks/<id>", methods=['GET'])
def show_park(id):
    park = park_repository.select(id)
    return render_template('parks/show.html', park = park)

#EDIT
@parks_blueprint.route("/parks/<id>/edit", methods=['GET'])
def edit_park(id):
    park = park_repository.select(id)
    return render_template('parks/edit.html', park = park)

#UPDATE
@parks_blueprint.route("/parks/<id>", methods=['POST'])
def update_park(id):
    name = request.form['name']
    park = Park(name, id)
    park_repository.update(park)
    return redirect("/parks")




