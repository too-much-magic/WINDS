import customtkinter

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
    text = city.get()
    for element in {title, subtitle, search_container}:
        element.destroy()
    frame.pack(pady=20, padx=60, expand=True, fill="both")
    
    
search_button = customtkinter.CTkButton(master=search_container, text="Search!", command=search)
search_button.pack(pady=12,padx=10,side='right')

root.mainloop()