#! /usr/bin/env python3
import requests

request_headers = {
  'User-agent': 'Shower thoughts bot'
}

response = requests.get('https://api.reddit.com/r/Showerthoughts', headers=request_headers)
response_json = response.json()
for entry in response_json['data']['children']:
    print('*', entry['data']['title'])

