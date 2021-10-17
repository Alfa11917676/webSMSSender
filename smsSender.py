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
    val = (df['phoneNumber'])
    i = 0
    for numbers in val:
        num = str(numbers)
        if num[0]=='9' and num[1]=='1':
            num = '+'+num
            num = num[3:]
        msg = textMsg.get("1.0", END)
        r = send_sms(num, msg)
        if r:
                        i += 1
        else:
            showerror("Error", f"Something went wrong with {num}..")
    print (i)
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
