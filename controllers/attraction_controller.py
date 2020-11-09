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
