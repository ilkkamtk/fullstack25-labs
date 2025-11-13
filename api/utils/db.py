from mongoengine import connect
import os

def mongo_connect():
    try:
        connection = connect(
            db=os.getenv("DB_NAME"),
            host=os.getenv("DATABASE_URL"),
        )
        print("DB connected successfully")
        print(connection)
        return connection
    except Exception as e:
        print("Connection to db failed:", str(e))
