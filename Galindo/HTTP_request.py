import requests

ip_address = 'http://20.127.202.175:8000'

response = requests.get(ip_address, headers={ 'X-Username': "chief.engineer" , 'X-Password': "ares-vallis-7"})
print(response.status_code)
print(response.text)
