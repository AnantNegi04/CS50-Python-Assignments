import requests

try:
    response = requests.get("rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
    print(response)
except requests.RequestException:
    print(Exception)