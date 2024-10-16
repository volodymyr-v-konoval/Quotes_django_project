import pymongo
import psycopg2
import uuid
from psycopg2 import sql
from psycopg2.extras import execute_values
from bson import ObjectId


def object_id_to_uuid(obj_id):
    return uuid.UUID(bytes=obj_id.binary + b'\x00' * 4)



mongo_client = pymongo.MongoClient("mongodb+srv://konoval:1985@cluster0.30d35.mongodb.net/")
mongo_db = mongo_client["hw08"]
mongo_collection1 = mongo_db["authors"]
mongo_collection2 = mongo_db["quotes"]

pg_conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="567234",
    host="localhost",
    port="5432"
)


pg_cursor = pg_conn.cursor()


mongo_data = list(mongo_collection2.find())

pg_table = "quotes_quote"
pg_columns = ["author_id", "tags", "quote"]


pg_data = []
for item in mongo_data:
    pg_item = (
        str(object_id_to_uuid(item["_id"])),
        str(object_id_to_uuid(item["author"])),
        item.get("tags", None),
        item.get("quote", None),
    )
    pg_data.append(pg_item)


insert_query = sql.SQL("INSERT INTO {} ({}) VALUES %s").format(
    sql.Identifier(pg_table),
    sql.SQL(", ").join(map(sql.Identifier, pg_columns))
)


execute_values(pg_cursor, insert_query, pg_data)


pg_conn.commit()
pg_cursor.close()
pg_conn.close()
mongo_client.close()
