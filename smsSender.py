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
    df = pd.read_csv('ph_nos.csv',index_col=None)
    val = (df['919477855936'])
    val = str(val)
    if val[0]=='9' and val[1]=='1':
        val = '+'+val
    print(val)
    df = df.to_json()
    print (type(df))
    print (df)

    # for index, number in df.iterrows():
    # # msg= textMsg.get("1.0", END)
    # # number  = textNumber.get()
    # # r = send_sms(number, msg)
    #     print( number)
    #     msg = textMsg.get("1.0", END)
    #     r = send_sms(number, msg)
    #     i = 0
    #     if r:
    #         showinfo("Send Success", "Successfully sent")
    #         i += 1
    #
    #     else:
    #         showerror("Error", f"Something went wrong with {number}..")

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
