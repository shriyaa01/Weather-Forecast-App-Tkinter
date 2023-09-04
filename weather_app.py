from tkinter import *
from tkinter import ttk
import requests
#this function is to get weather result
def get_report():
     city=city_name.get()
     data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1e7404d83a6d0c51e8321e1aedae4fa8").json()
     weather_climate_label1.config(text=data['weather'][0]['main'])
     weather_describtion_label1.config(text=data['weather'][0]['description'])
     temp_label1.config(text=str(round(data['main']['temp']-273.15,3))+"°C")
     humidity_label1.config(text=str(data['main']['humidity'])+"%")
     pressure_label1.config(text=str(data['main']['pressure'])+"mb")

#we have created a window here
win=Tk()
win.title("Weather Forecast App")
win.config(background="#3498db")
win.geometry('500x500')

#header
name_label=Label(win,text="Weather App",font=("Roboto",26,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

#combobox
city_name=StringVar()
indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
                 "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
                 "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
                 "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
state_combobox = ttk.Combobox(win, values=indian_states, font=("Roboto", 20),textvariable=city_name)
state_combobox.place(x=50,y=120,height=50,width=400)

#resultant label
weather_climate_label=Label(win,text="Weather Climate:",font=("Roboto",16),background="#3498db",foreground="white")
weather_climate_label.place(x=25,y=260,height=40,width=210)

weather_climate_label1=Label(win,text=" ",font=("Roboto",16),background="#3498db",foreground="white")
weather_climate_label1.place(x=245,y=260,height=40,width=210)

weather_describtion_label=Label(win,text="Weather Description:",font=("Roboto",16),background="#3498db",foreground="white")
weather_describtion_label.place(x=25,y=300,height=40,width=210)

weather_describtion_label1=Label(win,text=" ",font=("Roboto",16),background="#3498db",foreground="white")
weather_describtion_label1.place(x=245,y=300,height=40,width=210)

temp_label=Label(win,text="Temperature:",font=("Roboto",16),background="#3498db",foreground="white")
temp_label.place(x=25,y=340,height=40,width=210)

temp_label1=Label(win,text=" ",font=("Roboto",16),background="#3498db",foreground="white")
temp_label1.place(x=245,y=340,height=40,width=210)

humidity_label=Label(win,text="Humidity:",font=("Roboto",16),background="#3498db",foreground="white")
humidity_label.place(x=25,y=380,height=40,width=210)

humidity_label1=Label(win,text="",font=("Roboto",16),background="#3498db",foreground="white")
humidity_label1.place(x=245,y=380,height=40,width=210)

pressure_label=Label(win,text="Pressure:",font=("Roboto",16),background="#3498db",foreground="white")
pressure_label.place(x=25,y=420,height=40,width=210)

pressure_label1=Label(win,text=" ",font=("Roboto",16),background="#3498db",foreground="white")
pressure_label1.place(x=245,y=420,height=40,width=210)

# Create the "Search" button
search_button = Button(win, text="Search",font= ("Roboto", 18),bg= "Red",fg= "white",borderwidth= 2,width=10,command=get_report)
search_button.place(x=70,y=200,height=50,width=360)

#end
win.mainloop()