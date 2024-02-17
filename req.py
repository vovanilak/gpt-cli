import requests

url = "https://gigachat.devices.sberbank.ru/api/v1/models"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer NzM2YzBiYmYtYTMzZS00N2IxLWE3OGQtZDY2YzlmMTkyNWQ5OjNlNmM1YWEyLTU1ZGEtNDYwZi1iZjUzLWU1NGQzZjQyYzNmNg=='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)