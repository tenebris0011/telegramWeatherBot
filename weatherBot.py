import requests
import pyowm

# OWM Variables
owmKey = ''# You will need to get an API key from OWM https://openweathermap.org/api
location = ''# Set your location of choice.

# This is the basic setup for sending a message with the telegram bot.
def telegramBotSendtext(botMessage):
    
    botToken = ''# You can follow this link for setting up a telegram bot https://core.telegram.org/bots
    botChatID = ''# This will need to get the chat ID by going to Ex. https://api.telegram.org/bot000000:000000000000000000000/getUpdates
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&parse_mode=Markdown&text=' + botMessage

    responseText = requests.get(sendText)

    return responseText.json()

# This block of code will grab the weather information that you want. You can add more by going to the pyowm documenation https://pyowm.readthedocs.io/en/latest/
owm = pyowm.OWM(owmKey)
location = owm.weather_at_place(location)
weather = location.get_weather()
temp = str(round((weather.get_temperature('fahrenheit').get('temp'))))
status = (weather.get_detailed_status())

# These send the message to your chat.
statusMessage = telegramBotSendtext("Looking up you will see: " + status)
tempMessage = telegramBotSendtext("The current temperature is: " + temp+chr(176)+"F")
