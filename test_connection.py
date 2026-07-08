from database.connection import engine

try:
    with engine.connect() as connection:
        print("Databaseconnected sucessfully")
except Exception as e:
    print("Connection failed")
    print(e)
