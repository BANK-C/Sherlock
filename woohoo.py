import base64
import webbrowser

  # Go to example.com

encoded = base64.b64encode(open("1da78809-4321-4a8a-b098-16a61ea810fb.png", "rb").read()).decode()
webbrowser.open("data:text/html,"+encoded)
print(encoded)
#Code above is useless lol
#Code below returns json
#curl -X POST -u "apikey:it5MqoTbZ3aZhZM16P6baHVHyBvA6kwouL51KkDWTq2s" --form "images_file=@2f2599f0-171d-4ed3-a138-5c9b32f84ff0.png" --form "classifier_ids=detect_faces" "https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19"
