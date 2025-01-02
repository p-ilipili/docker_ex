import requests
import os

# Define the URL and users
url = 'http://api:8000/permissions'

users = [
    ('alice', 'wonderland'),
    ('bob', 'builder'),
    ('clementine', 'mandarine')
]


def test_credentials(username, password):
    response = requests.get(url, params={'username': username, 'password': password})
    if response.ok:
        outcome=f"Success: {response.json()}"
    else:
        outcome=f"Error: {response.status_code, response.text}"
    
    output = f'''
    ============================
        Authentication test
    ============================
    request done at "/permissions"
    | username="{username}"
    | password="{password}"
    test result: {outcome}
    '''

    if os.environ.get('LOG') == '1':
        with open('/api_log/api_test.log', 'a') as file:
            file.write(output)


for username, password in users:
    test_credentials(username, password)