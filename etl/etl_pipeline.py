import mysql.connector

DB_CONFIG = {
    "host": "dataBase",  # Nazwa kontenera MySQL z docker-compose
    "user": "user1",
    "password": "user1",
    "database": "weather_data"
}

def create_table():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_Europe (
        city VARCHAR(50),
        temperature FLOAT
    )
    """)

    print("Table 'weather' already exists.")

    # connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_table()
