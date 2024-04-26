import requests

def get_weather_forecast(api_key, city):
    # Base URL for the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the complete URL with the API key and city name
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Send an HTTP GET request to the OpenWeatherMap API
    response = requests.get(complete_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the weather data from the response
        data = response.json()
        
        # Extract relevant information from the response
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        # Print the weather forecast
        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Failed to retrieve weather data.")

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    
    # Specify the city for which you want to retrieve the weather forecast
    city = "New York"
    
    # Get the weather forecast for the specified city
    get_weather_forecast(api_key, city)

if __name__ == "__main__":
    main()
