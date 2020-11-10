from db.run_sql import run_sql
from models.park import Park


def save(park):
    sql= "INSERT INTO parks (name) VALUES (%s) RETURNING id"
    values = [park.name]
    results = run_sql(sql, values)
    park.id = results[0]['id']
    return park

def select_all():
    parks = []

    sql = "SELECT * FROM parks"
    results = run_sql(sql)

    for row in results:
        park = Park(row['name'], row['id'])
        parks.append(park)
    return parks

def select(id):
    park = None
    sql = "SELECT * FROM parks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        park = Park(result['name'], result['id'])
    return park

def delete_all():
    sql = "DELETE FROM parks"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM parks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(park):
    sql = "UPDATE parks SET (name) = (%s) WHERE id = %s"
    values = [park.name, park.id]
    run_sql(sql, values)
