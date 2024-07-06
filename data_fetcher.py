import requests
import sqlite3
import json

API_KEY = 'e4ada7ef9baa20e4d048ab88993e27c2'
CITY = 'London'  # You can change this to any city you want

# Fetch data from OpenWeatherMap API
def fetch_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

# Create database and table
def setup_database():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            description TEXT,
            humidity INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

# Insert data into the database
def insert_data(conn, data):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, temperature, description, humidity)
        VALUES (?, ?, ?, ?)
    ''', (CITY, data['main']['temp'], data['weather'][0]['description'], data['main']['humidity']))
    conn.commit()

def main():
    # Fetch weather data from API
    weather_data = fetch_weather_data()

    # Setup database
    conn = setup_database()

    # Insert fetched data into database
    insert_data(conn, weather_data)

    print(f"Weather data for {CITY} has been successfully fetched and stored in the database.")

    # Display the stored data
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        print("\nLast stored weather data:")
        print(f"City: {row[1]}")
        print(f"Temperature: {row[2]}°C")
        print(f"Description: {row[3]}")
        print(f"Humidity: {row[4]}%")
        print(f"Timestamp: {row[5]}")
    else:
        print("No data found in the database.")

    # Close the database connection
    conn.close()
if __name__ == "__main__":
    main()