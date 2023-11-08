# client.py

import requests
import json

url = "http://3.36.49.125:8000/log"

message_data = {
    "message": "This is a log message."
}

response = requests.post(url, 
                         data=json.dumps(message_data), 
                         headers={"Content-Type": "application/json"})

print(response.text)