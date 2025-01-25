import requests

jokeURL = 'https://official-joke-api.appspot.com/random_joke'

response = requests.get(jokeURL)

if response.status_code == 200:
    data = response.json()
    print('Here is a funny joke:')
    print(data['setup'] + "\n" + data['punchline'])
else:
    print('API Call Failed')