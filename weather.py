from tkinter import *
import requests
import json
from PIL import ImageTk,Image
root=Tk()

#loading images
my_img1=ImageTk.PhotoImage(Image.open(r'‪img_summer.jpg'))
my_img3=ImageTk.PhotoImage(Image.open(r'‪img_winter.jpg'))
my_img2=ImageTk.PhotoImage(Image.open(r'img_autum.jpg'))
e=Entry(root)
e.grid(row=0,column=0)


#reset function 

def des():
    mylabel.destroy()
    mylabel2.destroy()
    mylabel3.destroy()
    e.delete(0,END)

#fuction to hit api with pincode and get back a json file 

def call():
    url = "http://api.openweathermap.org/data/2.5/weather?zip="+e.get()+",in&appid=e38272bcc6592022ec2c45f73f070397"
    api_request=requests.get(url)
    api=json.loads(api_request.content)
    global mylabel,mylabel2,mylabel3
    mylabel=Label(root,text="temp........"+str(int(api['main']['temp'])-273))
    mylabel.grid(row=1,column=0)
    mylabel2=Label(root,text="location........."+api['name'])
    mylabel2.grid(row=1,column=1)
    if(int(api['main']['temp'])-273>33):
        mylabel3=Label(image=my_img1)
        mylabel3.grid(row=2,column=0)
    elif(int(api['main']['temp'])-273<33 and int(api['main']['temp'])-273>18):
        mylabel3=Label(image=my_img2)
        mylabel3.grid(row=2,column=0)
    elif(int(api['main']['temp'])-273<18):
        mylabel3=Label(image=my_img3)
        mylabel3.grid(row=2,column=0)
    print(api)

#find button

button1=Button(root,text="find",command=call)
button1.grid(row=0,column=1)

#reset button

button2=Button(root,text="reset",command=des)
button2.grid(row=0,column=2)

root.mainloop()