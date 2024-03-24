from weather_data import get_weather_data
from twilio.rest import Client


weather_data = get_weather_data()
#print(weather_data)


weather_code = [int(weather_data["list"][val]["weather"][0]["id"]) for val in range(0,4)]

message:str = "You can left your umbrella at home"
weather_code[2] = 600

for code in weather_code:
    print(code)
    if code < 700: 
        message = "Bring the ubrella with you, it is going to rain"
        break



AccountSID_Live="" 
Auth_Token_Live="" 

client = Client(AccountSID_Live, Auth_Token_Live)

message = client.messages.create(
  from_='+14253584238',
  body=message,
  to='+525516918487'
)

print(message.sid)


