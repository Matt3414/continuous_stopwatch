import tkinter as tk
from tkinter import filedialog
import time
import datetime
import os, pickle

window = tk.Tk()
window.title('Savable Timer')
btntext = tk.StringVar()
#varibles
timerstring = 'timer'
timerenable = False
timerSec = 0
timerVal = ""
fileName = "counter"

btntext.set("Start")
bigtimer = tk.Label(window,text=timerstring,font=("Arial", 30))
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
    global timerSec
    global fileName
    filePath = filedialog.asksaveasfile(defaultextension='.dat', initialfile=fileName+".dat",filetypes=[("Data Files", "*.dat"),("All Files","*.*")])
    print(filePath)
    if filePath != None:
        with open(filePath.name, 'w+b') as fp:
            pickle.dump(timerSec,fp)
            fp.close()
        print("Saved!")
    else: print("cancelled.")
saveBtn = tk.Button(window,text="Save",command=saveFile)

def newFileWithTimestamp():
    global timerSec
    global fileName
    
    timestamp = fileName + "_" + time.strftime("%Y%m%d_%H-%M-%S")
    filePath = filedialog.asksaveasfile(defaultextension='.dat', initialfile= timestamp + ".dat",filetypes=[("Data Files", "*.dat"),("All Files","*.*")])
    if filePath != None:
        with open(filePath.name, 'wb') as fp:
            pickle.dump(timerSec,fp)
            fp.close()
        print("Saved!")
    else: print("cancelled.")
timestampBtn = tk.Button(window,text="Save With Timestamp", command=newFileWithTimestamp)

def openFile():
    global timerSec
    filePath = filedialog.askopenfilename(initialdir= os.getcwd(), title="Open File", filetypes=[("Data Files","*.dat"), ("All Files", "*.*")])
    print(filePath)
    if filePath != '':
        file = open(filePath,"rb")
        unpickler = pickle.Unpickler(file)
        data = unpickler.load()
        timerSec = data
        bigtimer.configure(text= time.strftime("%H:%M:%S",time.gmtime(timerSec)))
        print(timerSec)
    else: print("cancelled.")
openBtn = tk.Button(window,text="Open File",command=openFile)

def reset():
    global timerSec
    timerSec = 0
    bigtimer.configure(text= time.strftime("%H:%M:%S",time.gmtime(timerSec)))
resetBtn = tk.Button(window,text="Reset", command=reset)

saveBtn.grid(row=1,column=2, padx=(10,10),pady=5)
openBtn.grid(row=1,column=1, padx=10,pady=5)
timestampBtn.grid(row=1,column=3, padx=(10,20),pady=5)

btn1.grid(row=2,column=1, padx=(10,10))
resetBtn.grid(row=2,column=2, padx= (20,20))
bigtimer.grid(row=3,column=1, columnspan= 3, pady= 30)


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