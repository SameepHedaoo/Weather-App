import tkinter as tk
import bs4
import json
import requests
from decouple import config
#Sameep Hedaoo
app = tk.Tk()
app.title("Weather App")
app.geometry("500x500")
app.resizable(False, False)
app.iconbitmap("cloudy.ico")

text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()
text4 = tk.StringVar()


text1.set("......")
text2.set("......")
text3.set("......")
text4.set(".............................")

Key = config('API_KEY')


def get_weather():
    city = box1.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid='+Key
    print(url)
    html = requests.get(url)
    hameep = bs4.BeautifulSoup(html.text, "html.parser")
    data = json.loads(hameep.text)

    temp = data["main"]["temp"] - 273.15
    hum = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    desc = data["weather"][0]["description"]
    weather_stat = data["weather"][0]["main"]
    weather_stat.lower()

    upper_desc = desc.upper()
    center = upper_desc.center(20," ")
    temp = "{:.2f}".format(temp)

    if weather_stat=="Rain":
        rain = tk.Label(app, text = "🌧", font= ("Segeo",55),fg="#33C4FF")
        rain.place(x=210,y=320)
    elif weather_stat=="Clouds":
        cloud = tk.Label(app, text = "🌥", font= ("Segeo",55),fg="orange")
        cloud.place(x=210,y=320)
    elif weather_stat=="Haze":
        haze = tk.Label(app, text = "🌫", font= ("Segeo",55),fg="grey")
        haze.place(x=210,y=320)
    elif weather_stat=="Mist":
        mist = tk.Label(app, text ="☁", font= ("Segeo",55),fg="silver")
        mist.place(x=210,y=320)
    elif weather_stat=="Clear":
        clear = tk.Label(app, text ="☀", font= ("Segeo",55),fg="orange")
        clear.place(x=210,y=320)

    text1.set(f"{temp}°C")
    text2.set(f"{hum}%")
    text3.set(wind_speed)
    text4.set(center)

label = tk.Label(app, text="Weather App☀", font=("Arial", 25), fg="#FFBE33")
label.place(x=120, y=2)

label1 = tk.Label(app, text="🌤", font=("Arial", 25), fg='orange')
label1.place(x=20, y=53, height=37)

box1 = tk.Entry(app, font=("Arial", 20), bg="silver", borderwidth=0,)
box1.place(x=60, y=60, width=340)

button1 = tk.Button(app, text="🔎", font=("Arial", 18), bg="white", borderwidth=0, command=get_weather)
button1.place(x=400, y=58, height=37)

label2 = tk.Label(app, text="Temperature \t|", font=("Arial", 15))
label2.place(x=20, y=100, height=50)

label3 = tk.Label(app, text=" Humidity\t|", font=("Arial", 15))
label3.place(x=210, y=100, height=50)

label4 = tk.Label(app, text="Wind", font=("Arial", 15))
label4.place(x=400, y=100, height=50)

temperature = tk.Label(app, textvariable = text1, font= ("Segeo",15))
temperature.place(x=60,y=200)
humidity = tk.Label(app, textvariable = text2, font= ("Segeo",15))
humidity.place(x=230,y=200)
windspeed = tk.Label(app, textvariable = text3, font= ("Segeo",15))
windspeed.place(x=400,y=200)
description = tk.Label(app, textvariable = text4, font= ("Segeo",15))
description.place(x=160,y=270)


app.mainloop()