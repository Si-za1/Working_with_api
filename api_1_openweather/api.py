import requests

def get_weather(api_key, city):
    # Define the API endpoint URL for current weather data
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()

            # Extract relevant weather information
            temperature = weather_data['main']['temp']
            temperature_min = weather_data ['main'] ['temp_min']
            timezone= weather_data ['timezone']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']

            # Print the weather information
            print(f'Weather in {city}:')
            print(f'Timezone:{timezone}')
            print(f'Temperature: {temperature}°C')
            print(f'Minimum temperature: {temperature_min}°C')
            print(f'Humidity: {humidity}%')
            print(f'Conditions: {description}')
        else:
            print(f'Error: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

if __name__ == '__main__':
   
    api_key = '3f348a31d875d8cba8adbf362b9a7482'
    
    # Input the city for which you want to get the weather
    city = input('Enter the city name: ')
    
    get_weather(api_key, city)
