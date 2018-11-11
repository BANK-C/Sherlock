import base64
import webbrowser
import os
import subprocess
import json
import requests 
from send_sms import *
from constants import *

API_ENDPOINT = "http://172.20.10.3:8090/speaker"
data = "<play_info><app_key>LLByt8cKG3OHgidKW5VG9hD9nm8SeMAh</app_key><url>https://00e9e64bace8714b1a3efd7fd6153cf17b9e5046034a84d4eb-apidata.googleusercontent.com/download/storage/v1/b/bank-c/o/No,%20Don't%20Touch%20That!%20-%20SOUND%20EFFECT%20(1).mp3?qk=AD5uMEtOzNGTVlvaBbH5462mBnV9X8uB7Ia6QEc2HP5OHb6dKH4i2y064v6iKN66E68MWcr__q2Az0Zq2GNoJf5gfsUFRzouNIEwF9fL_i9YOZCpjs2AVQ-qVpem5TEPgBFRaU2bAS-JMKm2TCO4h65K3ay5pBJuHACgVWEK3A-aBDTH734e-dWKs3Dtw82l2ZFCJaL9-wJ8yQN01Q8fvCpuebKExh19msF5_WlfdrRQplV4BlD40dA6LZAzUq30sgpDs5dMcmd-EmLBEyiQLQiKOM4AA_SPfDkWK5wIEUWnR4H8dqdrAtxFL13VKl9O8iDRf11aZ03CKnOyhOE_JVAaX2RJwGhK6lnj7GgV7X7noCJ4Q0-GAqtlIlf8ZmlgqBN7cY2VJZUwZkV_ir3LrSvXT3qS-eHIYo0WFk-Wclt93JZl9x3n2Q_jW9Gx4RF8SRRm_U02sK3v5xfTDsTlqx1diPflgn8YJuIpy3VtCkGcT20LuII38zDUutqbIlclHm6RkGF3eIrIkWgZpnVNIOImqN_dlD75EipU3HO7knDgfGsyX7YTEObarO1Khl9Ezmg-2E-Osaohx_VfDTmX4lZ-JO48EmP-28bnOVvMyG6HXRJ9-PBIVKYswksMdQqyZWA_Bpt0WdOQCymwUXlTZoNZHDsOI40Yc-H5NWjWBTpLVvBRv4WIf_ikeJfOR_iHPG6ruBxgmXObvB9sP6uLX22b51RbvXDPyaB2gNmTBS1VNOpKZkZKJVT7QuUZVwH1pcU1elvAV7l8TElNbxk1ncQ6WH0NrVu9Jj9qU30uNe0WvaWitJ7nU9E4QV05-yz8z6g7rcVZdVMe</url><service>SERVICE</service><reason>OPTIONAL</reason><message>OPTIONAL</message><volume>25</volume></play_info>"

#Code below returns json
#os.system('curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@test.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"')
#cmd = ['curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@test.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"']

str1 = 'curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@'+picture+'" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"'
#cmd = ['curl', '-X', 'POST', '-u', '"apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s"', '--form', '"images_file=@test.png"', '--form', '"classifier_ids=detect_faces"', '"https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"']
cmd = str1.split(" ")
#print(cmd)
result = subprocess.run(cmd, stdout=subprocess.PIPE)
output=subprocess.check_output(str1)
o_s = output.decode('utf-8')

json_acceptable_string = o_s.replace("'", "\"")
d = json.loads(json_acceptable_string)

age_json = d['images'][0]['faces'][0]['age']
age_range = str(age_json['min'])+"-"+str(age_json['max']) +" "
a_str = str(age_range)

if age_json["min"] < 5:
	output = "DON'T TOUCH THAT!"
	#r = requests.post(url = API_ENDPOINT, data = data) 
	#os.system("python send_sms.py")
	msg = "Your child is attempting to access your cabinet!"
elif age_json["min"] <25:
	output = "Hey there, college student! Snacks are to your left."
	msg = "The snacks are getting raided! Time to replenish?"
else:
	output = "Welcome to your cabinet! The food is to your right and the medicine is stored on the left."
	msg = "Your cabinet welcomes you ;)"


r = requests.post(url = API_ENDPOINT, data = data) 
send_sms(msg)
output += " You are probably "+a_str+ "years old."

text_file = open("Output.html", "w")
text_file.write('<html> \n')
text_file.write('<link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet"><link href="css/new-age.min.css" rel="stylesheet">')
text_file.write('<link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet"> \n')
text_file.write('<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet"> \n')
text_file.write('<link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet" \n>')
text_file.write('<link href="https://fonts.googleapis.com/css?family=Muli" rel="stylesheet">\n')

text_file.write('<div class="container h-100"><div class="row h-100"><div class="col-lg-7 my-auto"><div class="header-content mx-auto">')

text_file.write('<p> \n')
text_file.write(output)
text_file.write('</p> \n')

text_file.write('</div></div></div></div>')



text_file.write('</html>')
text_file.close()
#print(d['images'][0]['faces'][0]['age'])
#result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))
