import urllib3
import requests
import json

urllib3.disable_warnings()

def get_json(url, headers=None) -> 'dict': 
    restponse = requests.get(url, headers=headers)
    json = restponse.json()    
    return json

def get_token(url, headers, credentials) -> 'string': 
    response = requests.post(url, headers=headers, data=json.dumps(credentials), verify=False)
    return response.json()['token']
