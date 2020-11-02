# DX-API Provisioning script

This python script helps you to provision multiple LoRaWAN devices (listed in the _devices.csv_ file) through ThingPark DX-API.

1. Clone the repository and create a _config.json_ file:  
   `git clone https://github.com/norbertherbert/dxapi-provisioning.git`  
   `cd dxapi-provisioning`  
   `mv config_.json config.json`
2. Update the _apiBaseUrl_ property in the _config.json_ file.  
   The _apiBaseUrl_ value depends on your platform.  
   For example _dev1_ and _community_ platforms use: https://dx-api-dev1.thingpark.com while production platform use https://dx-api.thingpark.com
3. Update the _token_ property in the _config.json_ file.  
   You can generate an access token at the /getstarted endpoint of the API like: https://dx-api-dev1.thingpark.com/getstarted
4. Update/replace the _devices.csv_ file with your devices.  
   Please note that within the csv file the _deviceProfileId_, _connectivityPlanId_ and routingProfileId fields must have the value of a valid id.  
   You can list the valid resource ids with the _list_apiResource.py_ script.  
   (The script works only after you updated your _token_ in the _config.json_ file.)  
   `python list_apiResources.py deviceProfiles`  
   `python list_apiResources.py connectivityPlans`  
   `python list_apiResources.py routingProfiles`
5. Provision your devices by running the _provision.py_ script:  
   `python provision_devices.py devices.csv`
