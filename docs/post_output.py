
# importing the requests library 
import requests 
  
# defining the api-endpoint  
# API_ENDPOINT = "http://[SoundTouch product LAN IP Address]:8090/speaker"
API_ENDPOINT = "http://172.20.10.7:8090/speaker"  

# your API key here 
API_KEY = "k2S7Fyp2pEGXHtRXDHQtDlTE1K85ITS9"
URL = "https://github.com/BANK-C/Sherlock/blob/master/Kalimba.mp3"
SERVICE = "bank-c"

  
# data to be sent to api 
data = "<play_info><app_key>API_KEY</app_key><url>URL</url><service>SERVICE</service><volume>25</volume></play_info>"
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print(r.text) 
