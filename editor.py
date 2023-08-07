import tkinter as tk
from tkinter import filedialog, messagebox
import time
import datetime
import os,sys, pickle
import customfunctions as cf

def main():
    newTimer = 0
    window3 = tk.Tk()
    window3.title('timer editor')
    fileName = "counter"
    
    hoursText = tk.Label(window3, text="hours")
    minutesText = tk.Label(window3,text="minutes")
    secondsText = tk.Label(window3,text="seconds")
    hours = tk.Entry(window3)
    minutes = tk.Entry(window3)
    seconds = tk.Entry(window3)

    def openFile():
        global newTimer
        filePath = filedialog.askopenfilename(title="Open File", filetypes=[("Data Files","*.dat"), ("All Files", "*.*")])
        print(filePath)
        if filePath != '':
            newTimer = cf.readPickle(filePath,0,True)
            
            print(newTimer)
        else: print("cancelled.")
    importButton = tk.Button(window3,text="Import File", command=openFile)
    def saveFile():
        global newTimer
        global fileName
        filePath = filedialog.asksaveasfile(defaultextension='.dat', initialfile=fileName+".dat",filetypes=[("Data Files", "*.dat"),("All Files","*.*")])
        print(filePath)
        if filePath != None:
            cf.writePickle(filePath.name, newTimer)
            print("Saved!")
        else: print("cancelled.")
    saveButton = tk.Button(window3,text="Save", command=saveFile)

    hoursText.grid(row=2,column=1,padx=5)
    minutesText.grid(row=2,column=2,padx=5)
    secondsText.grid(row=2,column=3,padx=5)
    hours.grid(row=3,column=1,padx=5, pady=(5,10))
    minutes.grid(row=3,column=2,padx=5, pady=(5,10))
    seconds.grid(row=3,column=3,padx=5, pady=(5,10))

    window3.mainloop()

#uncomment for debug
main()