import requests
import pprint

# response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('via', 'A1!sAfE&PaSsWoRds2023'))
# pprint.pprint(response.json())

token = 'e8afb7c3e677ba4fe443b35573782b52eaf58fd6'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)
pprint.pprint(response.json())