import json, sys
from urllib import error
from urllib.request import Request, urlopen

def print_usage():
    print('usage: python delete_device.py <deviceReference>')

# Parse config file
try:
    config_file_json = open('config.json', 'r')
except OSError:
    print('cannot open: config.json')
    sys.exit(1)
config = json.load(config_file_json)

# Parse CLI params
if len(sys.argv) != 2 :
    print_usage()
    sys.exit(1)
deviceReference = sys.argv[1]

# Perform API request
req = Request(
    url = config['apiBaseUrl'] + '/core/latest/api/devices/' + deviceReference,
    headers = {
        'Accept': 'application/json; charset=UTF-8', 
        'Authorization': 'Bearer ' + config['token']
    },
    method = 'DELETE'
)
try:
    body = urlopen(req).read().decode('utf-8')
    print('------------------------')
    print('the device has been deleted')
    print('------------------------')
except error.HTTPError as err:
    body = err.read().decode('utf-8')
    print('------------------------')
    print(json.dumps(json.loads(body), indent=4))
    print('------------------------')
