import requests
def main(url):
    r = requests.get(url)
    j = (r.json())
    f = open('song.json', 'w+')
    f.write(j['data']['song']['data'])
    f.close()
    print(j['data']['song']['data'])
