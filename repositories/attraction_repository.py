from db.run_sql import run_sql
from models.park import Park
from models.land import Land
from models.attraction import Attraction

from repositories import park_repository
from repositories import land_repository

def save(attraction):
    sql= "INSERT INTO attractions (name, land_id, visited, visit_count, notes) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [attraction.name, attraction.land.id, attraction.visited, attraction.visit_count, attraction.notes]
    results = run_sql(sql, values)
    attraction.id = results[0]['id']
    return attraction

def select_all():
    attractions = []

    sql = "SELECT * FROM attractions"
    results = run_sql(sql)

    for row in results:
        land = land_repository.select(row['land_id'])
        attraction = Attraction(row['name'], land, row['visited'], row['visit_count'], row['notes'], row['id'])
        attractions.append(attraction)
    return attractions

def select(id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        land = land_repository.select(row['land_id'])
        attraction = Attraction(row['name'], land, row['visited'], row['visit_count'], row['notes'], row['id'])
    return attraction

def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(attractions):
    sql = "UPDATE attractions SET (name, land_id, visited, visit_count, notes) = (%s, %s, %s, %s, %s) WHERE is = %s"
    values = [attraction.name, attraction.land.id, attraction.visited, attraction.visit_count, attraction.notes]
    run_sql(sql, values)
