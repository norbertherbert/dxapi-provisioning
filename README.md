# DX-API Provisioning script
This python script helps you to provision multiple LoRaWAN devices (listed in the *devices.csv* file) through ThingPark DX-API.

1. Clone the repository and create a *config.json* file:  
`git clone https://github.com/norbertherbert/dxapi-provisioning.git`  
`cd dxapi-provisioning`  
`mv config_.json config.json`  
2. Update the *apiBaseUrl* property in the *config.json* file.
   The *apiBaseUrl* value depends on your platform.  
   For example *dev1* and *community* platforms use: https://dx-api-dev1.thingpark.com while production platform use https://dx-api.thingpark.com
3. Update the *token* property in the *config.json* file.
   You can generate an access token at the /getstarted endpoint of the API like: https://dx-api-dev1.thingpark.com/getstarted
4. Update/replace the *devices.csv* file with your devices.  
   Please note that within the csv file the *deviceProfileId* field must have the value of a valid id.  
   You can list the valid device profile ids with the *get_dev_profiles.py* script.  
   (The script works only after you updated your *token* in the *config.json* file.)  
   `python get_dev_profiles.py`  
5. Provision your devices by running the *provision.py* script:  
`python provisioning.py`
