"Ingrex is a python lib for ingress"
import requests
import re
import json

class Intel(object):
    "main class with all Intel functions"
    def __init__(self, cookies):
        token = re.findall(r'csrftoken=(\w*);', cookies)[0]
        self.headers = {
            'accept-encoding' :'gzip, deflate',
            'content-type': 'application/json; charset=UTF-8',
            'cookie': cookies,
            'origin': 'https://www.ingress.com',
            'referer': 'https://www.ingress.com/intel',
            'user-agent': 'Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'x-csrftoken': token,
        }
        self.refresh_version()

    def refresh_version(self):
        "refresh api version for request"
        request = requests.get('https://www.ingress.com/intel', headers=self.headers)
        self.version = re.findall(r'gen_dashboard_(\w*)\.js', request.text)[0]

    def fetch(self, url, payload):
        "raw request with auto-retry and connection check function"
        payload['v'] = self.version
        request = requests.post(url, data=json.dumps(payload), headers=self.headers)
        return request.json()['result']

    def fetch_map(self, tilekeys):
        "fetch game entities from Ingress map"
        url = 'https://www.ingress.com/r/getEntities'
        payload = {
            'tileKeys': tilekeys
        }
        return self.fetch(url, payload)

    def fetch_portal(self, guid):
        "fetch portal details from Ingress"
        url = 'https://www.ingress.com/r/getPortalDetails'
        payload = {
            'guid': guid
        }
        return self.fetch(url, payload)

if __name__ == '__main__':
    pass
