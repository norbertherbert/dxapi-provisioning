import json, csv
from urllib import error
from urllib.request import Request, urlopen

try:
    config_file_json = open('config.json', 'r')
except OSError:
    print('cannot open: config.json')
    quit()

config = json.load(config_file_json)

req = Request(url = config['apiBaseUrl'] + '/core/latest/api/deviceProfiles')
req.add_header('Accept', 'application/json')
req.add_header('Authorization', 'Bearer ' + config['token'])
try:
    body = urlopen(req).read().decode()
except error.HTTPError as e:
    body = e.read().decode('utf-8')
print('------------------------')
print(json.dumps(json.loads(body), indent=4))
print('------------------------')
