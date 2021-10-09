import requests
import json
from tkinter import *
import pandas as pd
from tkinter.messagebox import showinfo, showerror

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params ={
        'authorization': 'VDYS1vrljZxbWGzF0k3agf276dATisJHcLeEUQyRCwtu4OphBMNOPfdKzoIalyW8mxvp0T62tLXiFARJ',
        'sender_id': 'TXTIND',
        'message': message,
        'language': 'english',
        'route': 'v3',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')

def btn_click():
    df = pd.read_csv('ph_nos.csv')
    num = df['0']
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    i = 0
    if r:
        showinfo("Send Success", "Successfully sent")
        i += 1
        print(i)
    else:
        showerror("Error", "Something went wrong..")

root = Tk()
root.title("Message Sender ")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()
