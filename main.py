#项目开源地址：https://gitee.com/XShee/a-tool-to-base64
import tkinter as tk,base64
def encryptionFunction():
    print('To Encryption')
def decryptFunction():
    print('To Decrypt')
def main():
    #主窗口
    mainWindow=tk.Tk()
    #窗口标题
    mainWindow.title("一个加密/解密 文字/图片的开源小工具")
    #窗口图标
    mainWindow.iconbitmap('ico.ico')
    #设置窗口宽高
    mainWindow.geometry('900x500')
    #窗口的各种组件
    mainTitle=tk.Label(mainWindow,text="一款可以加密解密文字图片的开源小工具!",font=('Arial',14),width=40,height=3)
    buttonEncryption=tk.Button(mainWindow,text="加密文字/图片",width=30,height=17,bg='white',command=encryptionFunction)
    buttonDecrypt=tk.Button(mainWindow,text="解密文字/图片",width=30,height=17,bg='white',command=decryptFunction)
    
    #窗口组件放置区
    mainTitle.place(x=210,y=0)
    buttonEncryption.place(x=90,y=140)
    buttonDecrypt.place(x=570,y=140)
    
    #主窗口循环
    mainWindow.mainloop()
main()