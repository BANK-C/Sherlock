
# importing the requests library 
import requests 
  
# defining the api-endpoint  
# API_ENDPOINT = "http://[SoundTouch product LAN IP Address]:8090/speaker"
API_ENDPOINT = "http://172.20.10.7:8090/speaker"  

# your API key here 
API_KEY = "it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s"
URL = "https://github.com/BANK-C/Sherlock/blob/master/No%2C%20Don't%20Touch%20That!.mp3"
SERVICE = "bank-c"

  
# data to be sent to api 
data = "<play_info><app_key>API_KEY</app_key><url>URL</url><service>SERVICE</service></play_info>"
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
# pastebin_url = r.text 
# print("The pastebin URL is:%s"%pastebin_url) 
