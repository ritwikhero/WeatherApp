import tkinter as tk
import requests
from PIL import Image, ImageTk

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        wind_speed = weather['wind']['speed']
        press = weather['main']['pressure']
        humid = weather['main']['humidity']
        lat = weather['coord']['lat']
        long = weather['coord']['lon']

        final_str = 'City:%s \n Cobdition:%s \n Temperature(°C):%s \n Wind Speed (km/hr):%s \n Pressure(mb):%s \n Humidity(percent):%s \n Latitude:%s \n Longitude:%s' %(name, desc, temp,wind_speed, press,humid,lat,long )

    except:
        final_str = "No Record Found"

    return final_str

def weather(city):
    wkey = '9c147c384a95934d965e646a50beca38'
    link = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': wkey, 'q': city, 'units': 'Metric'}
    response = requests.get(link, params=parameters)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()
root.geometry('600x500')
root.title('Weather App')

img = "Milky Way.jfif"
bgs = ImageTk.PhotoImage(file=img, master=root)
bgs_lable = tk.Label(root, image=bgs)
bgs_lable.place(width=800, height=800)


frame = tk.Frame(root, bg='#99c2ff', bd=5, relief='ridge')
frame.place(relx=0.31, rely=0.1, relwidth=0.3, relheight=0.1, anchor='n')

frame1 = tk.Frame(root, bg='#99c2ff',bd=5, relief='ridge')
frame1.place(relx=0.65, rely=0.1, relwidth=0.3, relheight=0.1, anchor='n')

frame2 = tk.Frame(root, bg='#99c2ff', bd=5, relief='ridge')
frame2.place(relx=0.48, rely=0.2, relwidth=0.64, relheight=0.5, anchor='n')

entry = tk.Entry(frame, font=("times new roman",20))
entry.place(relheight=1, relwidth=1)

button = tk.Button(frame1, text="Search Weather", font=20, bg='#99c2ff', command=lambda: weather(entry.get()))
button.place(relx=0.15, relheight=1, relwidth=0.75)

label = tk.Label(frame2, font=('arial',16))
label.place(relwidth=1, relheight=1)
root.mainloop()
