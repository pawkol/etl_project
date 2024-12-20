import requests
import mysql.connector
from datetime import datetime

def extract(api_url, api_key, city):

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(api_url, params=params, verify=False)
    response.raise_for_status()

    return response.json()

def transform(data):

    utc_date = datetime.fromtimestamp(data['dt']) 
    return {
        'date': utc_date.strftime('%Y-%m-%d %H:%M:%S'),
        'hour': utc_date.strftime('%H:%M:%S'), 
        'temperature': data['main']['temp']
    }

def load(db_config, weather_data, table):

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    table_name = table

    insert_query = f"INSERT INTO {table_name} (date, time, temperature) VALUES (%s,%s,%s)"
    cursor.execute(insert_query, (weather_data['date'], weather_data['hour'], weather_data['temperature']))

    connection.commit()
    cursor.close()
    connection.close()

def main():

    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "apikey"     # paste your api key
    CITY = "Warsaw"
    table = "weather_Warsaw"

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
        load(DB_CONFIG, weather_data,table)


    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()