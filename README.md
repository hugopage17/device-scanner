# device-scanner
This python script was built to help assist with the troubleshooting process at Vital. 
It first prompts for an IP address and will run a basic ping to that address, if there is a response it will then run a basic http get request to that address to see if this device/address
can be accessed over a web browser. If the request is not found then it will open a desktop app that can be used to log into that device over. If the initial ip address does not return
a response on that first ping the script will then ping the next ip before it until a response it returned
