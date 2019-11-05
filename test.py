"""this is a test document"""

import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())
