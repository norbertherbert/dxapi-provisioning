# DX-API Provisioning script

1. Clone the repository and create a config.json file:  
`git clone https://github.com/norbertherbert/dxapi-provisioning.git`  
`cd dxapi-provisioning`  
`mv config_.json config.json`  
2. Update the "apiBaseUrl" property in the config.json file.
   The "apiBaseUrl" value depends on your platform.  
   For example the dev1 community platforms use: https://dx-api-dev1.thingpark.com while production platform use https://dx-api.thingpark.com
3. Update the token" property in the config.json file.
   You can generate an access token at the /getstarted endpoint of the API like: https://dx-api-dev1.thingpark.com/getstarted
3. Update/replace the "devices.csv" file with your devices.
4. Run the "provision.py" script:  
`python provisioning.py`
