#!/usr/bin/python3
import os
import sys
import tkinter as tk
import webbrowser
window = tk.Tk()
#创建窗口，定义为window
window.title('内容跳转')
#将窗口标题命名
window.geometry('400x300')
#设定窗口大小
label1 = tk.Label(window,text="在按下此按钮之前,请确认您已满18周岁",font='微软雅黑')
#输出内容
label1.pack()
def resource_path(relative_path):
    """获取程序中所需文件资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def command1():
    #设定函数command1
    webbrowser.open("https://www.bilibili.com/video/BV1gV411i7vq/?share_source=copy_web")
    window.quit()
button1 = tk.Button(window,text="确认",command=command1,width=10,height=2)
#定义按钮button1
gif = tk.PhotoImage(file=(resource_path("008.gif")))
#加载图片控件，载入图片
label2 = tk.Label(window,image=gif)
#在label2插入图片
label2.pack()
button1.pack()
window.mainloop()