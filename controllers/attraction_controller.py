from flask import Flask, render_template, request, redirect, Blueprint

from models.attraction import Attraction
from repositories import park_repository
from repositories import land_repository
from repositories import attraction_repository

attractions_blueprint = Blueprint("attractions", __name__)

@attractions_blueprint.route("/attractions")
def attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/index.html", attractions = attractions)

@attractions_blueprint.route("/still_to_see")
def still_to_see():
    attractions = attraction_repository.select_all()
    return render_template("attractions/still_to_see.html", attractions = attractions)

@attractions_blueprint.route("/seen")
def seen():
    attractions = attraction_repository.select_all()
    return render_template("attractions/seen.html", attractions = attractions)

#NEW
@attractions_blueprint.route("/attractions/new", methods=['GET'])
def new_attraction():
    attractions = attraction_repository.select_all()
    lands = land_repository.select_all()
    return render_template("attractions/new.html", attractions = attractions, lands = lands)

#CREATE
@attractions_blueprint.route("/attractions", methods=['POST'])
def create_attraction():
    name = request.form['name']
    land_id = request.form['land_id']
    visited = request.form['visited']
    visit_count = request.form['visit_count']
    notes = request.form['notes']
    land = land_repository.select(land_id)
    attraction = Attraction(name, land, visited, visit_count, notes)
    attraction_repository.save(attraction)
    return redirect("/still_to_see")

#SHOW
@attractions_blueprint.route("/attractions/<id>", methods=['GET'])
def show_attraction(id):
    attraction = attraction_repository.select(id)
    return render_template('attractions/show.html', attraction = attraction)

#EDIT
@attractions_blueprint.route("/attractions/<id>/edit", methods=['GET'])
def edit_attraction(id):
    attraction = attraction_repository.select(id)
    lands = land_repository.select_all()
    return render_template('attractions/edit.html', attraction = attraction, lands = lands)

#UPDATE
@attractions_blueprint.route("/attractions/<id>", methods=['POST'])
def update_attraction(id):
    name = request.form['name']
    land_id = request.form['land_id']
    visited = request.form['visited']
    visit_count = request.form['visit_count']
    notes = request.form['notes']
    land = land_repository.select(land_id)
    attraction = Attraction(name, land, visited, visit_count, notes, id)
    attraction_repository.update(attraction)
    return redirect("/attractions")