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
