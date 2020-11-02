# DX-API Provisioning script

1. Clone the repository and create a config.json file:
```
git clone https://github.com/norbertherbert/dxapi-provisioning.git
cd dxapi-provisioning
mv config_.json config.json
```
3. Edit "config.json" and update the "apiBaseUrl" and "token" properties
4. Update/replace the "devices.csv" file with your devices
5. Run the "provision.py" script: 
```
python provisioning.py
```
