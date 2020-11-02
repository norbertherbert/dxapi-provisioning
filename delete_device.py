import json, sys
from urllib import error
from urllib.request import Request, urlopen

if len(sys.argv) != 2 :
    print('usage: delete_device.py <device reference>')
    quit()

deviceReference = sys.argv[1]

try:
    config_file_json = open('config.json', 'r')
except OSError:
    print('cannot open: config.json')
    quit()

config = json.load(config_file_json)

req = Request(url = config['apiBaseUrl'] + '/core/latest/api/devices/' + deviceReference, method = 'DELETE')
req.add_header('Accept', 'application/json; charset=UTF-8')
req.add_header('Authorization', 'Bearer ' + config['token'])
try:
    body = urlopen(req).read().decode('utf-8')
    print('------------------------')
    print('the device has been deleted')
    print('------------------------')
except error.HTTPError as e:
    body = e.read().decode('utf-8')
    print('------------------------')
    print(json.dumps(json.loads(body), indent=4))
    print('------------------------')
