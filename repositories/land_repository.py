from db.run_sql import run_sql
from models.park import Park
from models.land import Land

from repositories import park_repository

def save(land):
    sql= "INSERT INTO lands (name, park_id, theme, visited) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [land.name, land.park.id, land.theme, land.visited]
    results = run_sql(sql, values)
    land.id = results[0]['id']
    return land

def select_all():
    lands = []

    sql = "SELECT * FROM lands"
    results = run_sql(sql)

    for row in results:
        park = park_repository.select(row['park_id'])
        land = Land(row['name'], park, row['theme'], row['visited'], row['id'])
        lands.append(land)
    return lands

def select(id):
    land = None
    sql = "SELECT * FROM lands WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        park = park_repository.select(result['park_id'])
        land = Land(result['name'], park, result['theme'], result['visited'], result['id'])
    return land

def delete_all():
    sql = "DELETE FROM lands"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM lands WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(land):
    sql = "UPDATE lands SET (name, park_id, theme, visited) = (%s, %s, %s, %s) WHERE is = %s"
    values = [land.name, land.park.id, land.theme, land.visited]
    run_sql(sql, values)
