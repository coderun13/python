import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY_HERE" #put api key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result_label.config(text=f"Temperature: {temp}°C\n"
                                     f"Condition: {desc.title()}\n"
                                     f"Humidity: {humidity}%\n"
                                     f"Wind Speed: {wind} m/s",
                                fg="#f1f1f1")
        else:
            messagebox.showerror("Error", "City Not Found!")
            
    except Exception as e:
        messagebox.showerror("Error", "Check your internet connection!")

#GUI Setup
root = tk.Tk()
root.title("Weather Pro")
root.geometry("400x400")
root.configure(bg="#212121")

title = tk.Label(root, text="WEATHER APP", font=("Helvetica", 20, "bold"), fg="cyan", bg="#212121")
title.pack(pady=20)

city_entry = tk.Entry(root, font=("Helvetica", 14), width=20, justify='center')
city_entry.pack(pady=10)
city_entry.insert(0, "Enter City Name")

search_btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12, "bold"), 
                       bg="cyan", fg="black", activebackground="#008b8b")
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#212121", justify="left")
result_label.pack(pady=20)

root.mainloop()