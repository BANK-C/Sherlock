
# importing the requests library 
import requests 
  
# defining the api-endpoint  
# API_ENDPOINT = "http://[SoundTouch product LAN IP Address]:8090/speaker"
API_ENDPOINT = "http://172.20.10.7:8090/speaker"  

# your API key here 
APP_KEY = "LLByt8cKG3OHgidKW5VG9hD9nm8SeMAh"
URL = "https://github.com/BANK-C/Sherlock/blob/master/Kalimba.mp3"
OPTIONAL = "optional"
SERVICE = "bank-c"

  
# data to be sent to api 
data = "<play_info><app_key>APP_KEY</app_key><url>URL</url><service>SERVICE</service><reason>OPTIONAL</reason><message>OPTIONAL</message><volume>25</volume></play_info>"
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print(r.text) 
