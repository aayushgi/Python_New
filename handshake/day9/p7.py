#Install requests package and fetch a webpage.
import requests
response=requests.get("https://github.com/")#link
print("status ",response.status_code)#if 200 then success
print(response.text[:300])#number of text