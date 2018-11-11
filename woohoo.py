import base64
import webbrowser
import os
import subprocess

#Code below returns json
#os.system('curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@test.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"')
#cmd = ['curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@test.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"']
str1 = 'curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@test.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"'
#cmd = ['curl', '-X', 'POST', '-u', '"apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s"', '--form', '"images_file=@test.png"', '--form', '"classifier_ids=detect_faces"', '"https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"']
cmd = str1.split(" ")
print(cmd)
result = subprocess.run(cmd, stdout=subprocess.PIPE)
output=subprocess.check_output(str1)
text_file = open("Output.txt", "w")
text_file.write(output.decode())
text_file.close()
print(output)
#result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))
