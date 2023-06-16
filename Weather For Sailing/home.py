from tkinter import *
from tkinter import ttk
import time
import requests
import tkinter
from tkinter import font
import tkinter as tk
from functools import partial
from PIL import Image, ImageTk, ImageFont
import threading

def get_wind_speed_category(speed):
    if speed < 5:
        return "Light"
    elif 6 <= speed <= 14:
        return "Normal"
    else:
        return "Windy"

def update_condition():
    while True:
        response = requests.get(base_url).json()
        wind_speed = response['wind']['speed']
        wind_category = get_wind_speed_category(wind_speed)
        condition_text.set("Sailing is " + wind_category + " today")
        time.sleep(10)


# Define the api key
city = 'Auckland'
api_key = "9522fe2047582e922d19ac9849c35ee6"

# Define the base url for the point forecast api
base_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

#window
tkWindow = Tk()
tkWindow.minsize(1400, 800)
tkWindow.maxsize(1400,800)
tkWindow.title('Weather For Sailors')

# Defining the fonts
normal_font = font.Font(family="Arial", size=20)
bold_font = font.Font(family="Arial", size=20, weight="bold")

condition_text = StringVar()

#creating label for the first weather variable
sailing_variable1 = Label(tkWindow, fg="red")
sailing_variable1.place(x=1, y=1)
print(font.families())

TitleLable = Label(tkWindow, textvariable=condition_text, font=("Arial", 30))
TitleLable.place(relx=0.5, y=20, anchor=tk.CENTER)

# Create a separate thread for updating the condition
update_thread = threading.Thread(target=update_condition)
update_thread.daemon = True
update_thread.start()

tkWindow.mainloop()