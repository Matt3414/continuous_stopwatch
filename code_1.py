import tkinter as tk
from tkinter import filedialog, messagebox
import time
import datetime
import os,sys, pickle

appicon = 'appicon2.ico'
#code to locate image in pyinstaller executeable: https://stackoverflow.com/questions/31836104
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('')
    return os.path.join(base_path,relative_path)

#custom seconds converter because time.strftime("%H:%M:%S",time.gmtime(timerSec)
#rolls over to 01:00:00 when seconds is greater than 89999.
def S_To_H_M_S(secondsIn: int, paddingEN: bool):
    MS = secondsIn%3600
    H = int(((secondsIn - MS)/3600))
    S = MS%60
    M = int(((MS - S)/60))
    if paddingEN == True:
        if S < 10:
            sPadding = "0"
        else:
            sPadding = ""
        if M < 10:
            mPadding = "0"
        else:
            mPadding = ""
        if H < 10:
            hPadding = "0"
        else:
            hPadding= ""
    else:
        mPadding= ""
        sPadding= ""
    Result  = str(hPadding + str(H) + ":" + mPadding + str(M) + ":" + sPadding +str(S))
    return Result

window = tk.Tk()
window.title('Savable Timer')
window.iconbitmap(resource_path(appicon))
btntext = tk.StringVar()
#varibles
timerstring = 'timer'
timerenable = False
timerSec = 0
timerVal = ""
fileName = "counter"

btntext.set("Start")
bigtimer = tk.Label(window,text=timerstring,font=("Arial", 30))
bigtimer.configure(text= S_To_H_M_S(timerSec,True))

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
    
    timestamp = fileName + "_" + time.strftime("%Y%m%d_%-I.%M-%S%p")
    timestamp = timestamp.replace(".",'\ua789', -1)
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
    filePath = filedialog.askopenfilename(title="Open File", filetypes=[("Data Files","*.dat"), ("All Files", "*.*")])
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
    bigtimer.configure(text= S_To_H_M_S(timerSec,True))
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
        timerVal = S_To_H_M_S(timerSec,True)
        print(timerSec)
        bigtimer.configure(text=timerVal)

def on_close():
    askToSave = True
    if askToSave:
        if messagebox.askyesno("Save Timer", "Do you want to save the timer before closing?"):
            saveFile()
        else:
            window.destroy()
    else: window.destroy()
window.after(1000,update)
window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()