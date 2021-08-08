# Make sure your firebase project's 'read' and 'write' rules are set to 'true'.
# Avoiding this step will lead to an error.

#############################################
##          Written by Rupak Poddar        ##
#############################################

from tkinter import*
import requests
import json

######### Your project ID goes here #########
project_ID = "YOUR PROJECT ID GOES HERE"
#############################################

url = "https://"+project_ID+".firebaseio.com/cmd"

def update_database(location, data, canvas, Status, highlights):
    client = requests.put(url+location+".json", "\""+data+"\"")
    get_status(canvas, Status, highlights)

def get_status(canvas, Status, highlights):
    client = requests.get(url+".json")
    if client.status_code == 200:
        canvas.itemconfig(Status, text="STATUS: CONNECTED", fill="green")
    else:
        canvas.itemconfig(Status, text="STATUS: UNABLE TO CONNECT", fill="red")
    decider = json.loads(client.text)
    if (decider["Device1"] == "ON"):
        canvas.coords(highlights[0], 90,90,245,185)
    if (decider["Device1"] == "OFF"):
        canvas.coords(highlights[0], 240,90,395,185)

    if (decider["Device2"] == "ON"):
        canvas.coords(highlights[1], 90,190,245,285)
    if (decider["Device2"] == "OFF"):
        canvas.coords(highlights[1], 240,190,395,285)

    if (decider["Device3"] == "ON"):
        canvas.coords(highlights[2], 90,290,245,385)
    if (decider["Device3"] == "OFF"):
        canvas.coords(highlights[2], 240,290,395,385)

    if (decider["Device4"] == "ON"):
        canvas.coords(highlights[3], 90,390,245,485)
    if (decider["Device4"] == "OFF"):
        canvas.coords(highlights[3], 240,390,395,485)

class button:
    def __init__(self, Text, Command, X, Y, canvas,):
        self.canvas = canvas
        self.color = "blue3"
        self.height = 3
        self.width = 10

        Button(canvas,
               text=Text,
               command=Command,
               height = self.height,
               width = self.width,
               font=("Sans",20),
               fg = self.color).place(x=X, y=Y)

root = Tk()
canvas = Canvas(root, width = 400, height = 510, bg="white")
canvas.pack()

watermark = canvas.create_text(320, 495, text="Rupak's Firebase controller", fill="black", font=("Sans",10))
Status = canvas.create_text(200, 40, text="STATUS: CONNECTING...", fill="black", font=("Sans",20))

box1 = canvas.create_rectangle(3, 3, 397, 82, outline="black")
box2 = canvas.create_rectangle(3, 85, 397, 507, outline="black")

highlight1 = canvas.create_rectangle(240,90,395,185,fill="red3")
highlight2 = canvas.create_rectangle(240,190,395,285,fill="red3")
highlight3 = canvas.create_rectangle(240,290,395,385,fill="red3")
highlight4 = canvas.create_rectangle(240,390,395,485,fill="red3")
highlights = [highlight1, highlight2, highlight3, highlight4]

label1 = canvas.create_text(50, 130, text="Device 1", fill="black", font=("Sans",20))
label2 = canvas.create_text(50, 230, text="Device 2", fill="black", font=("Sans",20))
label3 = canvas.create_text(50, 330, text="Device 3", fill="black", font=("Sans",20))
label4 = canvas.create_text(50, 430, text="Device 4", fill="black", font=("Sans",20))

ON1 = button("ON", lambda: update_database("/Device1", "ON", canvas, Status, highlights), 100, 100, canvas)
ON2 = button("ON", lambda: update_database("/Device2", "ON", canvas, Status, highlights), 100, 200, canvas)
ON3 = button("ON", lambda: update_database("/Device3", "ON", canvas, Status, highlights), 100, 300, canvas)
ON4 = button("ON", lambda: update_database("/Device4", "ON", canvas, Status, highlights), 100, 400, canvas)

OFF1 = button("OFF", lambda: update_database("/Device1", "OFF", canvas, Status, highlights), 250, 100, canvas)
OFF2 = button("OFF", lambda: update_database("/Device2", "OFF", canvas, Status, highlights), 250, 200, canvas)
OFF3 = button("OFF", lambda: update_database("/Device3", "OFF", canvas, Status, highlights), 250, 300, canvas)
OFF4 = button("OFF", lambda: update_database("/Device4", "OFF", canvas, Status, highlights), 250, 400, canvas)

get_status(canvas, Status, highlights)
root.mainloop()
