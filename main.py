import requests

api_key = "YOUR OPEN WEATHER API KEY"

MY_LAT = "YOUR LATITUDE"

MY_LONG = "YOUR LONGITUDE"

BOT_TOKEN = "TELEGRAM BOT TOKEN"

BOT_CHAITID = "TElEGRAM CHAT ID"

def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = BOT_CHAITID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    return requests.get(send_text)




parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12] #slice the list up to the 11th index

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"] #get the weather key, the first item and the id key
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    telegram_bot_sendtext("It's going to rain today, remember to bring an Umbrella.")
