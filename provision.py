import json, csv
from urllib import error
from urllib.request import Request, urlopen

try:
    config_file_json = open('config.json', 'r')
except OSError:
    print('cannot open: config.json')
    quit()

config = json.load(config_file_json)

try:
    devices_file_csv = open('devices.csv', 'r', encoding="utf-8-sig")
except OSError:
    print('cannot open: devices.csv')
    quit()

devices = csv.DictReader(devices_file_csv, delimiter=',')

for device in devices:

    data_json = json.dumps(device, indent=4)
    print('------------------------')
    print(data_json)
    print('------------------------')

    req = Request(url = config['apiBaseUrl'] + '/core/latest/api/devices', data = data_json.encode('utf-8'))
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')
    req.add_header('Authorization', 'Bearer ' + config['token'])
    try:
        body = urlopen(req).read().decode()
    except error.HTTPError as e:
        body = e.read().decode('utf-8')
    print('------------------------')
    print(json.loads(body))
    print('------------------------')