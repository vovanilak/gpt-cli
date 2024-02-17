import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload={}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)