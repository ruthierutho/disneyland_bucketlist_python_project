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