import psycopg2


def get_cursor():
    pg_conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="567234",
        host="localhost",
        port="5432"
    )
    pg_cursor = pg_conn.cursor()
    return pg_cursor


