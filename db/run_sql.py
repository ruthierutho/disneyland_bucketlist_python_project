import psycopg2
import psycopg2.extras as ext
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

def run_sql(sql, values = None):
    conn = None
    results = []

    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # conn=psycopg2.connect("dbname='disneyland_todo'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
