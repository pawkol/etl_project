import mysql.connector

DB_CONFIG = {
    "host": "dataBase",
    "user": "user1", 
    "password": "user1",
    "database": "weather_data"
}

def createTable():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_Warsaw (
        date DATE,
        hour TIME,
        temperature FLOAT
        )
        """)   

    cursor.close()
    connection.close()

if __name__ == "__main__":
    createTable()


