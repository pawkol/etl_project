import mysql.connector

DB_CONFIG = {
    "host": "dataBase",
    "user": "user1", 
    "password": "user1",
    "database": "weather_data"
}

city = {"Warsaw", "Berlin", "Paris", "Barcelona"}

def createTable():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    for x in city:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS weather_{x} (
            id AUTO_INCREMENT PRIMARY KEY,
            date DATE PRIMARY KEY,
            hour TIME,
            temperature FLOAT
            )
            """)   

    cursor.close()
    connection.close()

if __name__ == "__main__":
    createTable()


