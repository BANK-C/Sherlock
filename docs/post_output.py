
# importing the requests library 
import requests 
  
# defining the api-endpoint  
# API_ENDPOINT = "http://[SoundTouch product LAN IP Address]:8090/speaker"
API_ENDPOINT = "http://172.20.10.3:8090/speaker"  

# your API key here 
APP_KEY = "LLByt8cKG3OHgidKW5VG9hD9nm8SeMAh"
URL = "https://00e9e64bace8714b1a3efd7fd6153cf17b9e5046034a84d4eb-apidata.googleusercontent.com/download/storage/v1/b/bank-c/o/No,%20Don't%20Touch%20That!%20-%20SOUND%20EFFECT%20(1).mp3?qk=AD5uMEtOzNGTVlvaBbH5462mBnV9X8uB7Ia6QEc2HP5OHb6dKH4i2y064v6iKN66E68MWcr__q2Az0Zq2GNoJf5gfsUFRzouNIEwF9fL_i9YOZCpjs2AVQ-qVpem5TEPgBFRaU2bAS-JMKm2TCO4h65K3ay5pBJuHACgVWEK3A-aBDTH734e-dWKs3Dtw82l2ZFCJaL9-wJ8yQN01Q8fvCpuebKExh19msF5_WlfdrRQplV4BlD40dA6LZAzUq30sgpDs5dMcmd-EmLBEyiQLQiKOM4AA_SPfDkWK5wIEUWnR4H8dqdrAtxFL13VKl9O8iDRf11aZ03CKnOyhOE_JVAaX2RJwGhK6lnj7GgV7X7noCJ4Q0-GAqtlIlf8ZmlgqBN7cY2VJZUwZkV_ir3LrSvXT3qS-eHIYo0WFk-Wclt93JZl9x3n2Q_jW9Gx4RF8SRRm_U02sK3v5xfTDsTlqx1diPflgn8YJuIpy3VtCkGcT20LuII38zDUutqbIlclHm6RkGF3eIrIkWgZpnVNIOImqN_dlD75EipU3HO7knDgfGsyX7YTEObarO1Khl9Ezmg-2E-Osaohx_VfDTmX4lZ-JO48EmP-28bnOVvMyG6HXRJ9-PBIVKYswksMdQqyZWA_Bpt0WdOQCymwUXlTZoNZHDsOI40Yc-H5NWjWBTpLVvBRv4WIf_ikeJfOR_iHPG6ruBxgmXObvB9sP6uLX22b51RbvXDPyaB2gNmTBS1VNOpKZkZKJVT7QuUZVwH1pcU1elvAV7l8TElNbxk1ncQ6WH0NrVu9Jj9qU30uNe0WvaWitJ7nU9E4QV05-yz8z6g7rcVZdVMe"
OPTIONAL = "optional"
SERVICE = "bank-c"

  
# data to be sent to api 
data = "<play_info><app_key>LLByt8cKG3OHgidKW5VG9hD9nm8SeMAh</app_key><url>https://00e9e64bace8714b1a3efd7fd6153cf17b9e5046034a84d4eb-apidata.googleusercontent.com/download/storage/v1/b/bank-c/o/No,%20Don't%20Touch%20That!%20-%20SOUND%20EFFECT%20(1).mp3?qk=AD5uMEtOzNGTVlvaBbH5462mBnV9X8uB7Ia6QEc2HP5OHb6dKH4i2y064v6iKN66E68MWcr__q2Az0Zq2GNoJf5gfsUFRzouNIEwF9fL_i9YOZCpjs2AVQ-qVpem5TEPgBFRaU2bAS-JMKm2TCO4h65K3ay5pBJuHACgVWEK3A-aBDTH734e-dWKs3Dtw82l2ZFCJaL9-wJ8yQN01Q8fvCpuebKExh19msF5_WlfdrRQplV4BlD40dA6LZAzUq30sgpDs5dMcmd-EmLBEyiQLQiKOM4AA_SPfDkWK5wIEUWnR4H8dqdrAtxFL13VKl9O8iDRf11aZ03CKnOyhOE_JVAaX2RJwGhK6lnj7GgV7X7noCJ4Q0-GAqtlIlf8ZmlgqBN7cY2VJZUwZkV_ir3LrSvXT3qS-eHIYo0WFk-Wclt93JZl9x3n2Q_jW9Gx4RF8SRRm_U02sK3v5xfTDsTlqx1diPflgn8YJuIpy3VtCkGcT20LuII38zDUutqbIlclHm6RkGF3eIrIkWgZpnVNIOImqN_dlD75EipU3HO7knDgfGsyX7YTEObarO1Khl9Ezmg-2E-Osaohx_VfDTmX4lZ-JO48EmP-28bnOVvMyG6HXRJ9-PBIVKYswksMdQqyZWA_Bpt0WdOQCymwUXlTZoNZHDsOI40Yc-H5NWjWBTpLVvBRv4WIf_ikeJfOR_iHPG6ruBxgmXObvB9sP6uLX22b51RbvXDPyaB2gNmTBS1VNOpKZkZKJVT7QuUZVwH1pcU1elvAV7l8TElNbxk1ncQ6WH0NrVu9Jj9qU30uNe0WvaWitJ7nU9E4QV05-yz8z6g7rcVZdVMe</url><service>SERVICE</service><reason>OPTIONAL</reason><message>OPTIONAL</message><volume>25</volume></play_info>"
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print(r.text) 
