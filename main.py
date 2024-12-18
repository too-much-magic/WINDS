import customtkinter
import requests
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, expand=True)

title = customtkinter.CTkLabel(master=frame, text="Welcome to WINDS!", font=("Segue UI", 24))
title.pack(pady=4,padx=10)

subtitle = customtkinter.CTkLabel(master=frame, text="(a.k.a. Weather-based International Nuclear and Rainy Day Scale)", font=("Roboto", 12))
subtitle.pack(pady=4,padx=10)

search_container = customtkinter.CTkFrame(master=frame)
search_container.pack(pady=10,padx=10, expand=True,side='top')

city = customtkinter.CTkEntry(master=search_container, placeholder_text="City")
city.pack(pady=12, padx=10,side='left')

def search():
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        raise ValueError("API key is not set.")
    
    params = {
        'q' : city.get(),
        'key' : api_key,
        'aqi' : "yes",
        'days' : '7' # TODO: const for now, could change later
    }
    base_url = "http://api.weatherapi.com/v1/forecast.json"
        
    for element in {title, subtitle, search_container}:
        element.destroy()
    frame.pack(pady=20, padx=60, expand=True, fill="both")

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        weather_data = response.json()
        
        location = customtkinter.CTkLabel(master=frame, text=f"WINDS for {weather_data["location"]["name"]}:", font=("Roboto", 24) )
        location.pack(pady=12, padx=10)
        
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    
search_button = customtkinter.CTkButton(master=search_container, text="Search!", command=search)
search_button.pack(pady=12,padx=10,side='right')

root.mainloop()