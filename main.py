from tkinter import *
from tkinter import ttk
import requests


#function
def data_get():
     
     city = city_name.get()
     #API Calling
     data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=12b5fb0d60be22fc7cbc01f0290f7073").json()
     w_label1.config(text=data["weather"][0]["main"])
     wd_label1.config(text=data["weather"][0]["description"])
     temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
     pre_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather App")
win.config(bg="#3498db")
win.geometry("500x570")

name_label = Label(win, text="Weather App",font=("Time New Roman", 30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

#list of the place
city_name = StringVar()
list_name =["Dhaka","Chittagong","Sylhet", "Barisal","Khulna","Rajshahi"]
com = ttk.Combobox(win,text="Weather App",values=list_name,font=("Time New Roman", 20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)






#1st labels
w_label = Label(win, text="Weather Climate",font=("Time New Roman", 15,"bold"))
w_label.place(x=25,y=260,height=50,width=210)

#1st text
w_label1 = Label(win, text=" ",font=("Time New Roman", 20))
w_label1.place(x=250,y=260,height=50,width=210)


#2nd labels
wd_label = Label(win, text="Weather description",font=("Time New Roman", 15,"bold"))
wd_label.place(x=25,y=330,height=50,width=210)

#2nd text
wd_label1 = Label(win, text=" ",font=("Time New Roman", 20))
wd_label1.place(x=250,y=330,height=50,width=210)


#3rd labels
temp_label = Label(win, text="Temperature",font=("Time New Roman", 15,"bold"))
temp_label.place(x=25,y=400,height=50,width=210)

#3rd text
temp_label1 = Label(win, text=" ",font=("Time New Roman", 20))
temp_label1.place(x=250,y=400,height=50,width=210)


#4th labels
pre_label = Label(win, text="Pressure",font=("Time New Roman", 15,"bold"))
pre_label.place(x=25,y=470,height=50,width=210)

#4th text
pre_label1 = Label(win, text=" ",font=("Time New Roman", 20))
pre_label1.place(x=250,y=470,height=50,width=210)


#Button
done_button = Button(win,text="Get Weather",font=("Time New Roman", 15,"bold"),command=data_get)
done_button.place(y=190,height=50,width=250,x=120)

win.mainloop()