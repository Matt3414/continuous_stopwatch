import tkinter as tk
from tkinter import filedialog
import time
import os, pickle

window = tk.Tk()
window.title('Savable Timer')
frame1 = tk.Frame(window)

btntext = tk.StringVar()
btntext.set("Start")
timerstring = 'timer'
timerenable = False
timerSec = 0
timerVal = ""
bigtimer = tk.Label(window,text=timerstring,font=("Arial", 30))

file_path = 'file1.dat'
if os.path.exists(file_path):
    print("file already exsits!")
else:
    with open(file_path, 'wb') as fp:
        pickle.dump(0,fp)
        fp.close()

bigtimer.configure(text= time.strftime("%H:%M:%S",time.gmtime(timerSec)))

def timer():
    global timerenable
    if timerenable == False:
        timerenable = True
        btntext.set("Stop")
    else:
        timerenable = False
        btntext.set("Start")
    print(timerenable)
btn1 = tk.Button(window,textvariable=btntext, command=timer)

def saveFile():
    with open(file_path, 'wb') as fp:
        pickle.dump(timerSec,fp)
        fp.close()
    print("Saved!")
saveBtn = tk.Button(window,text="Save",command=saveFile)

def openFile():
    global timerSec
    filePath = 'file1.dat'
    file = open(filePath,"rb")
    unpickler = pickle.Unpickler(file)
    data = unpickler.load()
    timerSec = data
    bigtimer.configure(text= time.strftime("%H:%M:%S",time.gmtime(timerSec)))
    print(timerSec)
openBtn = tk.Button(window,text="Open File",command=openFile)

def reset():
    global timerSec
    timerSec = 0
    bigtimer.configure(text= time.strftime("%H:%M:%S",time.gmtime(timerSec)))
resetBtn = tk.Button(window,text="Reset", command=reset)

saveBtn.grid(row=1,column=1, padx=(50,10))
openBtn.grid(row=1,column=2, padx=(10,20))

btn1.grid(row=2,column=1, padx=(50,10))
resetBtn.grid(row=2,column=2, padx= (10,20))
bigtimer.grid(row=3,column=1, columnspan= 2, pady= 30)


def update():
    global timerSec
    
    window.after(1000,update)
    if(timerenable == True):
        timerSec += 1
        timerVal = time.strftime("%H:%M:%S",time.gmtime(timerSec))
        print(timerSec)
        bigtimer.configure(text=timerVal)
        
        
window.after(1000,update)
window.mainloop()