import requests
import os

# Define the URLs and users
urls = ['http://api:8000/v1/sentiment','http://api:8000/v2/sentiment']

users = [
    ('alice', 'wonderland'),
    ('bob', 'builder'),
]

sentence = "test sentence"

# Test function
def test_auth(username, password, url):
    response = requests.get(url, params={'username': username, 'password': password, 'sentence': sentence})
    if response.ok:
        outcome=f"Sentiment score: {response.json().get('score')}"
    else:
        outcome=f"Error: {response.status_code, response.text}"
    
    output = f'''
    ============================
        Authorization test
    ============================
    request done at "{url}"
    | username="{username}"
    | password="{password}"
    | sentence="{sentence}"
    {outcome}
    '''

    if os.environ.get('LOG') == '1':
        with open('/api_log/api_test.log', 'a') as file:
            file.write(output)

for url in urls:
    for username,password in users:
        test_auth(username, password, url)