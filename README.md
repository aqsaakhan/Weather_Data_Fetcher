# Weather Data Fetcher

This project fetches current weather data from the OpenWeatherMap API and stores it in a SQLite database.

## Project Description

Weather Data Fetcher is a Python-based application designed to demonstrate the ability to fetch data from an external API and store it in a local database. This project fulfills the requirements of a peer review assignment focused on API data retrieval and database management.

### Key Features:

1. **API Integration**: The application connects to the OpenWeatherMap API to fetch real-time weather data for a specified city.

2. **Database Management**: Utilizes SQLite to set up a local database, creating appropriate tables to store the retrieved weather information.

3. **Data Fetching and Storage**: Implements a mechanism to fetch weather data from the API and systematically store it in the SQLite database.

4. **Schema Setup**: Includes necessary database schema setup and migration scripts to ensure proper data structure.

5. **Configurable City Selection**: Allows users to easily modify the target city for weather data retrieval.

### Technical Highlights:

- Written in Python, demonstrating proficiency in scripting and API interactions.
- Uses the `requests` library for API calls and the built-in `sqlite3` module for database operations.
- Implements error handling for robust performance.
- Follows best practices in code organization and documentation.
## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup

1. Clone or download this repository to your local machine.

2. Open a command prompt or terminal and navigate to the project directory.

3. Install the required packages by running:

pip install -r requirements.txt

## Usage

1. Open the `weather_data_fetcher.py` file in a text editor.

2. (Optional) Modify the `CITY` variable to change the city for which you want to fetch weather data. By default, it's set to "London".

3. Run the script by executing the following command in your terminal:

python weather_data_fetcher.py

4. The script will fetch the current weather data for the specified city and store it in a SQLite database named `weather_data.db`.

5. Upon successful execution, you will see output similar to:

Weather data for London has been successfully fetched and stored in the database.
Last stored weather data:
City: London
Temperature: 15.5°C
Description: partly cloudy
Humidity: 76%
Timestamp: 2023-07-07 14:30:15

## File Structure

- `weather_data_fetcher.py`: The main Python script that fetches weather data and stores it in the database.
- `requirements.txt`: List of Python packages required for this project.
- `weather_data.db`: SQLite database file (created when the script is run) that stores the weather data.
- `README.md`: This file, containing project information and instructions.

## Database Schema

The script creates a `weather` table in the SQLite database with the following structure:

- `id`: INTEGER (Primary Key, Auto-increment)
- `city`: TEXT
- `temperature`: REAL
- `description`: TEXT
- `humidity`: INTEGER
- `timestamp`: DATETIME (Default: current timestamp)

## Troubleshooting

If you encounter any issues:

1. Ensure you have a working internet connection.
2. Verify that you've installed all required packages listed in `requirements.txt`.
3. Check that you have write permissions in the project directory (for creating the database file).

## Note

This project uses a free API key from OpenWeatherMap. If you plan to use this script extensively or for commercial purposes, please obtain your own API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).
