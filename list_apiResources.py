import json, sys
from urllib import parse, error
from urllib.request import Request, urlopen

def print_usage():
    print('usage: python list_apiResources.py <apiResource> [<pageIndex>]')
    print('<apiResource> = devices|deviceProfiles|connectivityPlans|routingProfiles|baseStations|baseStationProfiles')
    print('<pageIndex> is an integer. Numbering starts from 1. The page size is always 100.')

# Parse config file
try:
    config_file_json = open('config.json', 'r')
except OSError:
    print('cannot open: config.json')
    sys.exit(1)
config = json.load(config_file_json)

# Parse CLI params
if (len(sys.argv) < 2) or (len(sys.argv) > 3) :
    print_usage()
    sys.exit(1)
apiResource = sys.argv[1]
queryParams = {};
if len(sys.argv) == 3 :
    try:
        queryParams['pageIndex'] = int(sys.argv[2])
    except:
        print('Invalid <pageIndex>')
        print_usage()
        sys.exit(1)

# Perform API request
req = Request(
    url = config['apiBaseUrl'] + '/core/latest/api/' + apiResource + '?' + parse.urlencode(queryParams),
    headers = {
        'Accept': 'application/json; charset=UTF-8', 
        'Authorization': 'Bearer ' + config['token']
    },
    method = 'GET'
)
try:
    body = urlopen(req).read().decode('utf-8')
except error.HTTPError as e:
    body = e.read().decode('utf-8')
print('------------------------')
print(json.dumps(json.loads(body), indent=4))
print('------------------------')
