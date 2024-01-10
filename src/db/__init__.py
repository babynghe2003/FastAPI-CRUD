# from os import confstr_names, name
import pymongo

from .. import settings


# mongoClient = pymongo.MongoClient(
#     f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}"
#     f"@{settings.MONGO_HOST}:{settings.MONGO_PORT}/?authSource=admin"
# )
def init_db_connection():
    try:
        con_str = f"mongodb://{settings.MONGODB_USER}:{settings.MONGODB_PASS}@{settings.MONGODB_HOST}/?authSource=admin"

        mongoClient = pymongo.MongoClient(con_str)
        db = mongoClient[settings.MONGODB_NAME]
        return db, mongoClient
    except Exception as e:
        print(e)
        return None, None

def wrap_db_connection(func):
    def wrapper_function(*args, **kwargs):
        db, mongoClient = init_db_connection()
        if "db" in kwargs:
            kwargs.pop("db")
        result = func(*args, db=db, **kwargs)
        mongoClient.close()
        return result

    return wrapper_function
