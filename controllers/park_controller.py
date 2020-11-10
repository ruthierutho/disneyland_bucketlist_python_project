from flask import Flask, render_template, request, redirect, Blueprint

from models.park import Park
from repositories import park_repository
from repositories import land_repository
from repositories import attraction_repository

parks_blueprint = Blueprint("parks", __name__)

@parks_blueprint.route("/parks")
def parks():
    parks = park_repository.select_all()
    return render_template("parks/index.html", all_parks = parks)

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

