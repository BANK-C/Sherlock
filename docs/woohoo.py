import base64
import webbrowser
import os
import subprocess
import json
from constants import *

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
age_range = age_json['min']-age_json['max']
a_str = str(age_range)

if age_json["min"] < 5:
	output = "DON'T TOUCH THAT!"
else:
	output = "Welcome to your cabinet!"

output += "You are probably "+a_str+ "years old"

text_file = open("Output.txt", "w")
text_file.write(output)
text_file.close()
#print(d['images'][0]['faces'][0]['age'])
#result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))