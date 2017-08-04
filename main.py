import requests

def hello(event, context):
    url = 'https://api.ipify.org/?format=json'

    raw = requests.get(url)
    print raw

    result = raw.json()
    print result

    return result
