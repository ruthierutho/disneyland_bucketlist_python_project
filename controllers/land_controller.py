from flask import Flask, render_template, request, redirect, Blueprint

from models.land import Land
from repositories import park_repository
from repositories import land_repository
from repositories import attraction_repository

lands_blueprint = Blueprint("lands", __name__)

@lands_blueprint.route("/lands")
def lands():
    lands = land_repository.select_all()
    return render_template("lands/index.html", lands = lands)

#NEW
@lands_blueprint.route("/lands/new", methods=['GET'])
def new_land():
    lands = land_repository.select_all()
    parks = park_repository.select_all()
    return render_template("lands/new.html", lands = lands, parks = parks)

#CREATE
@lands_blueprint.route("/lands", methods=['POST'])
def create_land():
    name = request.form['name']
    park_id = request.form['park_id']
    visited = request.form['visited']
    park = park_repository.select(park_id)
    land = Land(name, park, visited)
    land_repository.save(land)
    return redirect("/attractions")

#SHOW
@lands_blueprint.route("/lands/<id>", methods=['GET'])
def show_land(id):
    land = land_repository.select(id)
    return render_template('lands/show.html', land = land)

#EDIT
@lands_blueprint.route("/lands/<id>/edit", methods=['GET'])
def edit_land(id):
    land = land_repository.select(id)
    parks = park_repository.select_all()
    return render_template('lands/edit.html', land = land, parks = parks)

#UPDATE
@lands_blueprint.route("/lands/<id>", methods=['POST'])
def update_land(id):
    name = request.form['name']
    park_id = request.form['park_id']
    visited = request.form['visited']
    park = park_repository.select(park_id)
    land = Land(name, park, visited, id)
    land_repository.update(land)
    return redirect("/lands")


