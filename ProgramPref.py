import tkinter as tk
from tkinter import filedialog, messagebox
import time
import datetime
import os,sys, pickle

scales = {"100%","200%","400%","800%"}
elementScale = 1
defaultBtnSize = 10
settingsChanged = False
settingsFile = "settings.dat"
def readSetBinary():
    with open(settingsFile, "rb") as frb:
        frb


def main():
    settingsRead = open(settingsFile,"rb")
    settingsList1 = pickle.load(settingsRead)
    
    window2 = tk.Tk()
    scale = tk.StringVar(window2)
    SaveCloseVal= tk.IntVar()
    SaveCloseVal.set(settingsList1[1])
    scale.set("100%")
    window2.title("Settings")
    #window2.geometry("300x150")
    saveOnCloseBtn = tk.Checkbutton(window2,text="Save on Close",variable=SaveCloseVal)
    scalingText = tk.Label(window2,text="Window Scale:")
    scaleSelector = tk.OptionMenu(window2,scale,*scales)
    
    def refreshSettings():
        print("ok")
        #from code_1 import updateElements
        #from code_1 import defaultBtnSize
        defaultBtnSizeStr = scale.get()
        saveOnLoad = SaveCloseVal.get()
        if(defaultBtnSizeStr == "100%"): elementScale = 1
        if(defaultBtnSizeStr == "200%"): elementScale = 2
        if(defaultBtnSizeStr == "400%"): elementScale = 4
        if(defaultBtnSizeStr == "800%"): elementScale = 8
        saveOnCloseBtn.configure(font=("arial", defaultBtnSize * elementScale))
        scalingText.configure(font=("arial", defaultBtnSize * elementScale))
        scaleSelector.configure(font=("arial", defaultBtnSize * elementScale))
        saveBtn.configure(font=("arial", defaultBtnSize * elementScale))
        settingsChanged = True
        settingsList = [saveOnLoad,elementScale]
        with open(settingsFile,"wb") as fb:
            pickle.dump(settingsList,fb)
        print(settingsList)
        window2.destroy()
    
    def readScale(*args):
        print(scale.get())
        print(SaveCloseVal.get())
        window2.destroy()
    saveBtn = tk.Button(window2,text="Save",command=refreshSettings)
        
    #scale.trace('w',readScale)
    #item arrangement
    saveOnCloseBtn.grid(row=1,column=1,padx=10)
    scalingText.grid(row=2,column=1,padx=10)
    scaleSelector.grid(row=2,column=2)
    saveBtn.grid(row=3,column=3,padx=5,pady=(20,5))
    window2.mainloop()

    
    
    
#uncomment for debug
#main()