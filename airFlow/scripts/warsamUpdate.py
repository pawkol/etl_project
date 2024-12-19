import requests
import mysql.connector
from datetime import datetime

def extract(api_url, api_key, city):

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()

def transform(data):

    return {
        'date': datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': data['main']['temp']
    }

def load(db_config, weather_data):

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    insert_query = "INSERT INTO weather (date, temperature) VALUES (%s, %s)"
    cursor.execute(insert_query, (weather_data['date'], weather_data['temperature']))

    connection.commit()
    cursor.close()
    connection.close()

def main():

    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "apiKey"
    CITY = "Warsaw"

    DB_CONFIG = {
        "host": "dataBase",
        "user": "user1", 
        "password": "user1",
        "database": "weather_data"
    }

    try:

        raw_data = extract(API_URL, API_KEY, CITY)
        weather_data = transform(raw_data)
        print(f"Transformed data: {weather_data}")
        load(DB_CONFIG, weather_data)


    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()