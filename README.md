# DX-API Provisioning script

Clone the repository and create a config.json file:
```
git clone https://github.com/norbertherbert/dxapi-provisioning.git
cd dxapi-provisioning
mv config_.json config.json
```
Edit "config.json" and update the "apiBaseUrl" and "token" properties  
Update/replace the "devices.csv" file with your devices  
Run the "provision.py" script: 
```
python provisioning.py
```
