import requests
import pandas as pd
import mysql.connector

DB_CONFIG = {
    "host": "dataBase",
    "user": "user1", 
    "password": "user1",
    "database": "weather_data"
}

def extract_weather_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

def transform_weather_data(raw_data):
    
    df = pd.DataFrame(raw_data["list"]) 
    
    df = df[df["name"] == "Warsaw"]
    
    transformed_data = df[["dt", "main.temp"]] 
    transformed_data.columns = ["date", "temperature"]
    
    transformed_data["date"] = pd.to_datetime(transformed_data["date"], unit='s').dt.strftime('%Y-%m-%d')
    
    return transformed_data

def load_data_to_db(data):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    for _, row in data.iterrows():
        cursor.execute(
            "INSERT INTO weather_Warsaw (date, temperature) VALUES (%s, %s)",
            (row["date"], row["temperature"])
        )
    
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    API_URL = "http://api.openweathermap.org/data/2.5/find?q=Warsaw&cnt=1&appid=YOUR_API_KEY"
    
    raw_data = extract_weather_data(API_URL)
    transformed_data = transform_weather_data(raw_data)
    load_data_to_db(transformed_data)
    print("ETL process completed successfully!")
