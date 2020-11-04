import json, csv, sys
from urllib import parse, error
from urllib.request import Request, urlopen

def print_usage():
    print('usage: python verify_devices.py <CSV file>')

# Parse config file
try:
    with open('config.json', 'r') as config_file_json:
        config = json.load(config_file_json)        
except OSError:
    print('cannot open: config.json')
    sys.exit(1)

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

    queryParams = { 'deviceEUI' : device['EUI']}

    req = Request( 
        url = config['apiBaseUrl'] + '/core/latest/api/devices?' + parse.urlencode(queryParams), 
        headers = {
            'Accept': 'application/json; charset=UTF-8', 
            'Authorization': 'Bearer ' + config['token']
        },
        method = 'GET'
    )
    try:
        body = urlopen(req).read().decode('utf-8')
        provisionedDevices = json.loads(body)
        if len(provisionedDevices) == 0:
            print('WARNING: EUI ' + device['EUI'] + ' is not provisioned!')
        else:
            print(body)
    except error.HTTPError as err:
        body = err.read().decode('utf-8')
        print(body)

