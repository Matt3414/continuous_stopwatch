import tkinter as tk
from tkinter import filedialog, messagebox
import time
import datetime
import os,sys, pickle
import customfunctions as cf

scales = {"100%","200%","400%","800%"}
saveBtnStates = {"no","yes"}
elementScale = 1
lastElementScale = 1
defaultBtnSize = 10
settingsChanged = False
settingsFile = "settings.pkl"

def main():
    global SaveCloseVal
    global elementScale
    if(cf.readPickle(settingsFile,[1,1],False) == 0): cf.writePickle(settingsFile,[1,1])
    settingsList1 = cf.readPickle(settingsFile,[1,1],False)

    window2 = tk.Tk()
    scale = tk.StringVar(window2)
    SaveCloseVal= tk.StringVar(window2)
    SaveCloseVal.set("yes")
    window2.title("Settings")
    print(settingsList1)
    #SaveCloseVal.set(bool(settingsList1[0]))
    scale.set(f"{settingsList1[1]}00%")
    lastElementScale = settingsList1[1]
    print(bool(settingsList1[0]))
    if(bool(settingsList1[0])):
        SaveCloseVal.set("yes")
    else:
        SaveCloseVal.set("no")
    #window2.geometry("300x150")
    #saveOnCloseBtn = tk.Checkbutton(window2,text="Save on Close",variable=SaveCloseVal,onvalue="on",offvalue="off")
    saveOnExitText = tk.Label(window2,text="Save on exit?")
    saveOnCloseDrop = tk.OptionMenu(window2,SaveCloseVal,*saveBtnStates)
    scalingText = tk.Label(window2,text="Window Scale:")
    scaleSelector = tk.OptionMenu(window2,scale,*scales)
    
    def refreshDropdown(*args):
        global saveOnLoad
        print("ok")
        defaultBtnSizeStr = scale.get()
        saveOnLoad = SaveCloseVal.get()
        global elementScale
        if(defaultBtnSizeStr == "100%"): elementScale = 1
        if(defaultBtnSizeStr == "200%"): elementScale = 2
        if(defaultBtnSizeStr == "400%"): elementScale = 4
        if(defaultBtnSizeStr == "800%"): elementScale = 8
        if(SaveCloseVal.get() == "yes"): saveOnLoad = 1
        if(SaveCloseVal.get() == "no"): saveOnLoad = 0
        cf.configureAll(window2.grid_slaves(),defaultBtnSize * elementScale)
        settingsChanged = True
    refreshDropdown()
    scale.trace_add("write",refreshDropdown)
    #SaveCloseVal.trace_add("write",refreshDropdown)
    def refreshSettings():
        global SaveCloseVal
        global elementScale
        global saveOnLoad
        if(SaveCloseVal.get() == 'yes'): saveOnLoad = 1
        if(SaveCloseVal.get() == 'no'): saveOnLoad = 0
        #saveOnLoad = SaveCloseVal1.get()
        print(saveOnLoad)
        cf.writePickle(settingsFile,[saveOnLoad,int(elementScale)])
        settingsList1 = cf.readPickle(settingsFile,[1,1],False)
        print(settingsList1)
        print(SaveCloseVal.get())
        #cf.configureAll(window2.grid_slaves(),defaultBtnSize * settingsList1[1])
        #window2.destroy()
        
    
    def readScale(*args):
        print(scale.get())
        print(SaveCloseVal.get())
        window2.destroy()
    saveBtn = tk.Button(window2,text="Save",command=refreshSettings)
    def StopPanel():
        window2.destroy()
        
    #scale.trace('w',readScale)
    #item arrangement
    saveOnExitText.grid(row=1,column=1,padx=5)
    saveOnCloseDrop.grid(row=1,column=2,padx=10)
    scalingText.grid(row=2,column=1,padx=10)
    scaleSelector.grid(row=2,column=2)
    saveBtn.grid(row=3,column=3,padx=5,pady=(20,5))
    
    window2.mainloop()
    

    
    
#uncomment for debug
#main()