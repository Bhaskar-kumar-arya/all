import requests
import tkinter as tk
import json

def GetWeather (cityName : str) -> dict :
    print("getting weather of",cityName)
    url = f"http://api.weatherapi.com/v1/current.json?key=a8bf5947de4a4e6083e180501252506&q={cityName}&aqi=no"
    return requests.get(url).json()
def Button_GetWeather () :
    result = ""
    for key,value in GetWeather(city_entry.get()).items() : 
        result += f"{key} : {value} \n"
    result_label.config(text=(result))

if __name__ == "__main__" : 
    root = tk.Tk()
    root.title = "Weather app"
    root.geometry("500x500")
    
    city_label = tk.Label(root,text="city name : ")
    city_label.pack(pady=5)

    city_entry = tk.Entry(root)
    city_entry.pack(pady=5)

    GetWeatherButton = tk.Button(root,text="Get Weather",command=Button_GetWeather)
    GetWeatherButton.pack(pady=5)

    result_label = tk.Label(root,text="")
    result_label.pack(pady=10)

    root.mainloop()