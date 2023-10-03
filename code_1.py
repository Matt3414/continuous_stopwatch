import tkinter as tk
from tkinter import filedialog, messagebox
import time
import datetime
import os,sys, json
import ProgramPref
#from ProgramPref import settingsChanged
import customfunctions as cf
import threading

appicon = 'appicon2.ico'

window = tk.Tk()
window.title('Savable Stopwatch V1.2.0')
window.iconbitmap(cf.resource_path(appicon))
frame_container = tk.Frame(window)

btntext = tk.StringVar()
#varibles
timerstring = 'timer'
timerenable = False
timerSec = 0
timerVal = ""
fileName = "counter"
defaultBtnSize = 10
defaultTextSize  = 30
#prefrencesFile = "prefrences.dat"
settingsFile = "settings.pkl"
sizeVar = 1
btntext.set("Start")
bigtimer = tk.Label(window,text=timerstring,font=("Arial", 30))
bigtimer.configure(text= cf.S_To_H_M_S(timerSec,True))
lastSize = 1
window.resizable(0,0)
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
    filePath = filedialog.asksaveasfile(defaultextension='.json', initialfile=fileName+".json",filetypes=[("json Files", "*.json"),("All Files","*.*")])
    print(filePath)
    if filePath != None:
        cf.writeJSON(filePath.name, timerSec,"seconds")
        print("Saved!")
    else: print("cancelled.")
saveBtn = tk.Button(window,text="Save",command=saveFile)

def newFileWithTimestamp():
    global timerSec
    global fileName
    
    timestamp = str(fileName + "_" + time.strftime("%Y%m%d_%I.%M-%S%p"))
    timestamp = timestamp.replace(".",'\ua789', -1)
    filePath = filedialog.asksaveasfile(defaultextension='.json', initialfile= timestamp + ".json",filetypes=[("Data Files", "*.json"),("All Files","*.*")])
    if filePath != None:
        cf.writeJSON(filePath.name,timerSec,"seconds")
        print("Saved!")
    else: print("cancelled.")
timestampBtn = tk.Button(window,text="Save With Timestamp", command=newFileWithTimestamp)

def openFile():
    global timerSec
    filePath = filedialog.askopenfilename(title="Open File", filetypes=[("json Files","*.json"), ("All Files", "*.*")])
    print(filePath)
    if filePath != '':
        readJSON = cf.readJSON(filePath,0,True,"seconds")
        timerSec = readJSON[0]
        bigtimer.configure(text= time.strftime("%H:%M:%S",time.gmtime(timerSec)))
        print(timerSec)
    else: print("cancelled.")
openBtn = tk.Button(window,text="Open File",command=openFile)

def reset():
    global timerSec
    timerSec = 0
    bigtimer.configure(text= cf.S_To_H_M_S(timerSec,True))
resetBtn = tk.Button(window,text="Reset", command=reset)

def prefrences():
    ProgramPref.main()
settingsBtn = tk.Button(window,text="Settings...",command=prefrences)

def refresh():
    settings = cf.readPickle(settingsFile,[1,1],False)
    cf.configureAll(window.grid_slaves,settings[1] * defaultBtnSize)

saveBtn.grid(row=1,column=2, padx=(10,10),pady=5)
openBtn.grid(row=1,column=1, padx=10,pady=5)
timestampBtn.grid(row=1,column=3, padx=(10,20),pady=5)

btn1.grid(row=2,column=1, padx=(10,10))
resetBtn.grid(row=2,column=2, padx= (20,20))
settingsBtn.grid(row=2,column=3, padx= (0,20))
bigtimer.grid(row=3,column=1, columnspan= 3, pady= 30)

def update():
    global timerSec
    
    window.after(1000,update)
    if(timerenable == True):
        timerSec += 1
        timerVal = cf.S_To_H_M_S(timerSec,True)
        print(timerSec)
        bigtimer.configure(text=timerVal)

def checkSize():
    global lastSize
    global defaultBtnSize
    while True:
        settings = cf.readPickle(settingsFile,[1,1],False)
        if (settings[1] != lastSize):
            cf.configureAll(window.grid_slaves(),settings[1] * defaultBtnSize)
            bigtimer.configure(font=("arial", 30 * settings[1]))
            lastSize = settings[1]
        time.sleep(0.1)
def on_close():
    global timerSec
    settings = cf.readPickle(settingsFile,[1,1],False)
    askToSave = bool(settings[0])
    if askToSave and timerSec > 0:
        print (timerSec)
        if messagebox.askyesno("Save Timer", "Do you want to save the timer before closing?"):
            saveFile()
            window.destroy()
        else:
            window.destroy()
    else: window.destroy()
t= threading.Thread(target=checkSize)
t.start()
window.after(1000,update)
window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()