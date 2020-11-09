from db.run_sql import run_sql
from models.park import Park


def save(park):
    sql= "INSERT INTO parks (name) VALUES (%s) RETURNING id"
    values = [park.name]
    results = run_sql(sql, values)
    park.id = results[0]['id']
    return park