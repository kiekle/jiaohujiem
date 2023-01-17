import os
import sys
import tkinter as tk
from playsound import playsound
root =  tk.Tk()
root.title("只音盒")
root.geometry('567x600')
root.resizable(0,0)
def resource_path(relative_path):
    """获取程序中所需文件资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
root.iconbitmap(resource_path("005.ico"))    
def sing():
    playsound(resource_path('1.mp3'))
    root.quit()
def sing1():
    playsound(resource_path('3.mp3'))
    root.quit()    
gif = tk.PhotoImage(file=(resource_path("002.gif")))
label1 = tk.Label(root,image=gif).pack()       
button1 = tk.Button(root,text="只因叫",width=40,height=5,command=sing,background="yellow").pack(side="left")
button2 = tk.Button(root,text="扣逼叫",width=50,height=5,command=sing1,background="green").pack(side="left")    
root.mainloop()