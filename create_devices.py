import json, csv, sys
from urllib import parse, error
from urllib.request import Request, urlopen

def print_usage():
    print('usage: python provision_devices.py <CSV file>')

# Parse config file
try:
    config_file_json = open('config.json', 'r')
except OSError:
    print('cannot open: config.json')
    sys.exit(1)
config = json.load(config_file_json)

# Parse CLI params
if (len(sys.argv) != 2) :
    print_usage()
    sys.exit(1)
apiResource = sys.argv[1]

# Parse CSV file
try:
    devices_file_csv = open(sys.argv[1], 'r', encoding="utf-8-sig")
except OSError:
    print("cannot open: %s" % sys.argv[1] )
    sys.exit(1)
devices = csv.DictReader(devices_file_csv, delimiter=',')

# Perform API requests
for device in devices:

    data_json = json.dumps(device, indent=4)
    print('------------------------')
    print(data_json)
    print('------------------------')

    req = Request( 
        url = config['apiBaseUrl'] + '/core/latest/api/devices', 
        data = bytes(data_json.encode('utf-8')),
        headers = {
            'Content-Type': 'application/json; charset=UTF-8', 
            'Accept': 'application/json; charset=UTF-8', 
            'Authorization': 'Bearer ' + config['token']
        },
        method = 'POST'
    )
    try:
        body = urlopen(req).read().decode('utf-8')
    except error.HTTPError as err:
        body = err.read().decode('utf-8')
    print('------------------------')
    print(json.loads(body))
    print('------------------------')
