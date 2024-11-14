"""Gets news articles"""

from flask import Flask, jsonify
import requests

app = Flask(__name__)

api_key = "1e46363f408a4e85ac5075c0a6297d70"

@app.route('/get_business_news', methods=['POST'])
def get_business_news():
    """Gets top 3 business headlines in the US right now"""
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"
    response = requests.get(url)
    # Dictionary to store results
    results = {'first': {}, 'second': {}, 'third': {}}
    # Only return the top 3 news articles
    if response.status_code == 200:
        # Convert response
        response = response.json()
        # Gets sub dictionary with the key 'articles'
        articles = response['articles']
        # Gets top 3 articles
        for i, article in enumerate(articles[:3]):
            # Each article goes into a specific entry in the results dictionary
            key = list(results.keys())[i]
            results[key]['title'] = article['title']
            results[key]['url'] = article['url']
            results[key]['publishedAt'] = article['publishedAt']
        return jsonify(results)
    else:
        print("Attempt to get news articles was unsuccessful")

@app.route('/get_bbc_news', methods=['POST'])
def get_bbc_news():
    """Returns top 3 headlines from BBC News"""
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}'
    response = requests.get(url)
    print(response.json())
    # Dictionary to store results
    results = {'first': {}, 'second': {}, 'third': {}}
    # Only return the top 3 news articles
    if response.status_code == 200:
        # Convert response
        response = response.json()
        print(response)
        # Gets sub dictionary with the key 'articles'
        articles = response['articles']
        print(articles)
        # Gets top 3 articles
        for i, article in enumerate(articles[:3]):
            # Each article goes into a specific entry in the results dictionary
            key = list(results.keys())[i]
            results[key]['title'] = article['title']
            results[key]['url'] = article['url']
            results[key]['publishedAt'] = article['publishedAt']
        print(results)
        return jsonify(results)
    else:
        print("Attempt to get news articles was unsuccessful")

if __name__ == '__main__':
    app.run(debug=True, port=5002)
