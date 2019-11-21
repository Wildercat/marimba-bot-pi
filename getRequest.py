import requests
import json
def main(url):
    r = requests.get(url)
    j = (r.json())
    print(j['results'][0]['name'])
    return json.loads(r.text)
main('https://randomuser.me/api/')