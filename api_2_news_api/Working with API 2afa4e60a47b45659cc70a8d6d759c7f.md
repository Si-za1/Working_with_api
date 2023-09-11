# Working with API

Owner: haruite to
Created time: September 8, 2023 10:13 AM

# **Working with the OpenWeatherMap API**

### **API Endpoint and API Key**

**API Endpoint**:

- The root endpoint for OpenWeatherMap's weather API is **`http://api.openweathermap.org/data/2.5/weather`**.
- To retrieve weather data for a specific city, you need to provide the **`q`** parameter with the city's name.
- Your unique **API key** is required to authenticate your requests and can be obtained from your OpenWeatherMap account under "My API Keys."

**API Request URL**:

- The complete API request URL should look like this:
    
    ```bash
    bashCopy code
    http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}
    
    ```
    

### **Important API Terminologies**

**Endpoint**:

- The root endpoint is the starting point of the API you're accessing.

**Root Path**:

- The root path specifies the resource you're requesting. It's like selecting a service in an automated phone system.

**Query Parameters**:

- Query parameters allow you to modify your request with key-value pairs.
- They start with a question mark (**`?`**) and use ampersands (**`&`**) to separate parameters.

### **Common HTTP Status Codes**

- **200**: Success.
- **401**: Unauthorized. Indicates issues with your API key.
- **404**: Error page. Resource not found.

### **Extracting Data from the API Response**

You can access specific data from the API response using Python dictionary indexing. For example:

```python

temperature = weather_data['main']['temp']
temperature_min = weather_data['main']['temp_min']
timezone = weather_data['timezone']
humidity = weather_data['main']['humidity']
description = weather_data['weather'][0]['description']

```

- **`weather_data`** is the variable holding the API response.
- Use descriptive variable names for clarity.
- The structure of the JSON response is available in the **[API documentation](https://openweathermap.org/current)**, allowing you to extract data as needed.

### **Example: Extracting Weather Description**

If you want to extract the weather description from the API response:

```python
Check out the JSON format first, check whether it has nested data or not, and then make sure you write it correctly:
For example:
"weather": [
    {
      "id": 501,
      "main": "Rain",
      "description": "moderate rain",
      "icon": "10d"
    }
  ],
```

extracting description from the above JSON data would be:

```jsx

weather_description = weather_data['weather'][0]['description']

```

Where:

- **`weather_description`** is the variable name.
- **`weather_data`** holds the API response.

By following these steps, you can access various weather parameters and use them in your Python application.

---

# NEWS API

### API Endpoint and API Key

**API Endpoint**:

- The root endpoint for the News API is **`https://newsapi.org/v2/`**.
- To retrieve news data for a specific topic, you need to provide the **`q`** parameter with the topic's name.
- Your unique **API key** is required to authenticate your requests and can be obtained from your News API account.

**API Request URL**:

- The complete API request URL should look like this:
    
    ```bash
    
    <https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}>
    
    ```
    

### Important API Terminologies

**Endpoint**:

- The root endpoint is the starting point of the API you're accessing.

**Root Path**:

- The root path specifies the resource you're requesting. It's like selecting a service in an automated phone system.

**Query Parameters**:

- Query parameters allow you to modify your request with key-value pairs.
- They start with a question mark (**`?`**) and use ampersands (**`&`**) to separate parameters.

### Common HTTP Status Codes

- **200**: Success.
- **401**: Unauthorized. Indicates issues with your API key.
- **404**: Error page. Resource not found.

### Extracting Data from the API Response

You can access specific data from the API response using Python dictionary indexing. For example:

```python
Title = news_data.article['title']
```

- **`news_data`** is the variable holding the API response.
- Use descriptive variable names for clarity.
- The structure of the JSON response is available in the **[API documentation](https://newsapi.org/docs)**, allowing you to extract data as needed.

### Example: Extracting Article Title

If you want to extract the article title from the API response:

```python
Check out the JSON format first, check whether it has nested data or not, and then make sure you write it correctly:
For example:
 "articles": [
    {
      "source": {
        "id": "cnn",
        "name": "CNN"
      },
      "author": "Analysis by Chris Cillizza, CNN Editor-at-large",
      "title": "How Joe Manchin just made life very difficult for Joe Biden",
      "description": "On Friday morning, Sen. Joe Manchin made clear that he was a "no" on the $3.5 trillion reconciliation package that Democrats had hoped to pass in the Senate and House this fall.",
      "url": "<https://www.cnn.com/2021/09/03/politics/joe-manchin-joe-biden-reconciliation-package/index.html>",
      "urlToImage": "<https://cdn.cnn.com/cnnnext/dam/assets/210902093725-02-joe-manchin-0902-super-tease.jpg>",
      "publishedAt": "2021-09-03T17:16:18Z",
      "content": "(CNN)On Friday morning, Sen. Joe Manchin made clear that he was a "no" on the $3.5 trillion reconciliation package that Democrats had hoped to pass in the Senate and House this fall. \\r\\n"
    }
  ],

```

extracting title from the above JSON data would be:

```jsx
article_title = news_data['articles'][0]['title']

```

Where:

- **`article_title`** is the variable name.
- **`news_data`** holds the API response.

By following these steps, you can access various news parameters and use them in your Python application.