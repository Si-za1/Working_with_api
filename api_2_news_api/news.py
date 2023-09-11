import requests

def get_top_news(api_key, country_code, num_articles=5):
    # Set the endpoint URL
    url = f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}'

    # Define query parameters
    params = {
        'apiKey': api_key,
        'country': country_code,
        'pageSize': num_articles,
    }

    try:
        # Send a GET request to the News API
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            news_data = response.json()

            # Extract and return the top news articles
            return news_data['articles']

        else:
            print(f"Error: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

if __name__ == '__main__':
    # Replace 'YOUR_API_KEY' with your actual News API key
    api_key = '6cb8cb5c26eb4b1cb906615fbdb2e38d'

    # Replace 'YOUR_COUNTRY_CODE' with the appropriate country code (e.g., 'US' for United States)
    #check the documentation for the country code. 
    country_code = 'jp'

    # Get the top 5 news articles
    top_news = get_top_news(api_key, country_code, num_articles=5)

    # Display the top news articles
    print("Top 5 News Articles of the Day:")
    for i, article in enumerate(top_news, start=1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Published At: {article['publishedAt']}")
        print(f"   Description: {article['description']}\n")
