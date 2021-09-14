# import requests
# from twilio.rest import Client
#
# api_key = "5e11972d9ed5c35497df0d88db9ea4bc"
#
# account_sid = "ACa813ab0b1de3a898fd29d8d583cdb324"
# auth_token = "6604b073d79b4e271f880d60c8c1f7bf"
#
# my_latitude = 23.0225
# my_longitude = 72.5714
#
# parameters = {
#     "lat": my_latitude,
#     "lon": my_longitude,
#     "appid": api_key,
#     "exclude": "current,daily,minutely"
# }
#
# response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response.raise_for_status()
# weather_data = response.json()
#
# weather_slice = weather_data["hourly"][18:24]
# will_rain = False
# for hour_data in weather_slice:
#     weather_condition_code = hour_data["weather"][0]["id"]
#     if weather_condition_code < 700:
#         will_rain = True
#
# if will_rain:
#     # print("Bring an Umbrella.")
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Bring an umbrella ☔☂🌂.",
#         from_="+14243634188",
#         to="+919016453372"
#     )
#     print(message.status)



import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "5e11972d9ed5c35497df0d88db9ea4bc"

account_sid = "ACa813ab0b1de3a898fd29d8d583cdb324"
auth_token = "6604b073d79b4e271f880d60c8c1f7bf"

my_latitude = 23.0225
my_longitude = 72.5714

parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:20]
will_rain = False
for hour_data in weather_slice:
    weather_condition_code = hour_data["weather"][0]["id"]
    if weather_condition_code < 700:
        will_rain = True

if will_rain:
    # print("Bring an Umbrella.")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☔☂🌂.",
        from_="+14243634188",
        to="+919016453372"
    )
    print(message.status)
