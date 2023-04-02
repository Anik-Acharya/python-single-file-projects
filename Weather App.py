import gtts  
from playsound import playsound
import requests
import json

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
weatherDic = json.loads(r.text)
temperature=weatherDic["current"]["temp_c"]
condition=weatherDic["current"]["condition"]["text"]
audio_text=f"currently in {city} the temperature is {temperature} degree celcius, and the weather condition is {condition}"

t1 = gtts.gTTS(audio_text)  
t1.save("sound.mp3")
playsound("sound.mp3")