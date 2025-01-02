import requests
import os

# Define the URLs and users
urls = ['http://api:8000/v1/sentiment','http://api:8000/v2/sentiment']

username = 'alice'
password = 'wonderland'

sentences = [('good','life is beautiful'),('bad','that sucks')]

# Test function
def test_content(username, password, url, sentiment, sentence):
    response = requests.get(url, params={'username': username, 'password': password, 'sentence': sentence})
    if response.ok:
        score = response.json().get('score')
        if score >= 0 and sentiment == 'good':
            outcome=f"The score corresponds with the sentiment of the sentence. Sentiment score: {score}"
        elif score < 0 and sentiment == 'bad':
            outcome=f"The score corresponds with the sentiment of the sentence. Sentiment score: {score}"
        else:
            outcome=f"The score does not correspond with the sentiment of the sentence. {score}"
    else:
        outcome=f"Error: {response.status_code, response.text}"
    
    output = f'''
    ============================
        Content Test
    ============================
    request done at "{url}"
    | username="{username}"
    | password="{password}"
    | sentiment : "{sentiment}" and sentence : "{sentence}"
    {outcome}
    '''

    if os.environ.get('LOG') == '1':
        with open('/api_log/api_test.log', 'a') as file:
            file.write(output)

for url in urls:
    for sentiment, sentence in sentences:
        test_content(username, password, url, sentiment, sentence)