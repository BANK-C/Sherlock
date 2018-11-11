import base64
import webbrowser
import os
import subprocess
import json
import requests 
from send_sms import *
from constants import *

API_ENDPOINT = "http://172.20.10.3:8090/speaker"
data = "<play_info><app_key>LLByt8cKG3OHgidKW5VG9hD9nm8SeMAh</app_key><url>https://00e9e64bac2b299c6556317d0e7dbb096fe450eced9767a795-apidata.googleusercontent.com/download/storage/v1/b/bank-c/o/No,%20Don't%20Touch%20That!%20-%20SOUND%20EFFECT.mp3?qk=AD5uMEvlWvRA8hqYQLuF_dkHjFsg9JffKOZFWxqncIq9-5z3EQJqnIg5Hu4Q-BWD-bjhep6Xoyl_3nJ5GFfRmjte0G1nbG2PIaOUxQEyiVWqHTB-lqcZj6Mk4jc8q9cxfy2W70unEfom-A5b434EWwBY2ba_1fj8zO3pVQ7f_beJRbRcvZrztIRCHcs0K6h0vtSc-lGFjcITcFI9qDYnR2qPssSscqDFG99ZDOKnOmijvmb7MWUgnMC3k6CO98Zyk1gSzO9RmMkfl1aeNR7iPEopHh8clOsFeoofpTakLUVI2MRzat6OOEGne4zNOJzUmTcjVWNGQeGsjExMrEcUqKtYqoaB1Ge_MK0a_uVn-QBsfF1ixMdTibkg4jd6iK5ki6g_G8lT6eU3s386eiyugIE9pizw-ZvhqcHcz_mAVjwmkaLGMuTt7TQofySSLbhbn4KTsdOirwGtFLbv5f28uYP7BBuqCtNMxQcLagNH_xRw0Zs-rKBpu6k4Ziozzzpky5CsOF3GENFQONUACS-0WJzDu7WfIF3hVJIWviMt7htXCdI8Er6w_yZG_88u8cKFXKcU3KoNs3CEHsfR26e5j0W_0GSN-A28BQwbOnw4jiN0h_WKuhsM1HM8MA2uvgPnaNO8Wc3auS2Y7e4h6sFWEaCAPSd-ZCE3xPX6LemGp3WH-ThhI9hy5v2cWU4ogCLxPUTNV3qy5V5pRwb_FlvHaTuwog402dcOjha0hOuV8ie6c03Ux-n8niLsjXv2AHu5Qur2CUjXjBIQNjL6URNJvAd5MnUR1nd_wqs-6Yr-NZ4eRodohi5JabXdxxxpkTdbHwRgapclDSnB</url><service>SERVICE</service><reason>OPTIONAL</reason><message>OPTIONAL</message><volume>25</volume></play_info>"

#Code below returns json
#os.system('curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@test.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"')
#cmd = ['curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@test.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"']

str1 = 'curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@'+"test.png"+'" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"'
#cmd = ['curl', '-X', 'POST', '-u', '"apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s"', '--form', '"images_file=@test.png"', '--form', '"classifier_ids=detect_faces"', '"https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"']
cmd = str1.split(" ")
print(cmd)
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
