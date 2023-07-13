#项目开源地址：https://gitee.com/XShee/a-tool-to-base64
import tkinter as tk,base64,os
def dencryptTextEnterFunction():
    global deputyLabel,backButton
    toDen=open("./File/toFile/toEnc.teXS","r")
    toDen=toDen.readline().encode("utf-8")
    denc=base64.b85decode(toDen).decode("utf-8")
    enterButton.place_forget()
    deputyLabel=tk.Label(mainWindow,text=f"解密后的内容为{denc}\n当然，它也被保存到了./File/toFile/den.txt中",font=('Arial',14))
    den=open("./File/toFile/den.txt","w")
    den.write(denc)
    den.close()
    backButton=tk.Button(mainWindow,text="返回",width=10,height=3,command=a2)
    backButton.place(x=380,y=350)
    deputyLabel.place(x=230,y=250)
def a2():
    main(2)
def a1():
    main(1)
def enterEncryptionButtonFunction():
    global backButton,deputyLabel
    toEncValue=enterLabel.get().encode("utf-8")
    EncValue=base64.b85encode(toEncValue).decode("utf-8")
    backButton=tk.Button(mainWindow,text="返回",width=10,height=3,command=a1)
    deputyLabel=tk.Label(mainWindow,text=f"加密后的内容为{EncValue}\n当然，它也被保存到了./File/toFile/toEnc.teXS中",font=('Arial',14))
    deputyLabel.place(x=230,y=250)
    ff=os.path.exists('./File/toFile')
    if not ff:
        os.makedirs('./File/toFile')
    toEnc=open("./File/toFile/toEnc.teXS",'w')
    toEnc.write(EncValue)
    toEnc.close()
    backButton.place(x=380,y=350)
def encryptionTextFunction():
    global enterLabel,enterButton
    print('encryptionText')
    #组件摧毁区
    encryptionImageButton.place_forget()
    encryptionTextButton.place_forget()
    buttonDecrypt.place_forget()
    buttonEncryption.place_forget()
    #加密文字组件区
    mainTitle=tk.Label(mainWindow,text="请输入要加密的文字",font=('Arial',14),width=40,height=3)
    enterLabel=tk.Entry(mainWindow,width=25)
    enterButton=tk.Button(mainWindow,text="确认",width=5,height=1,command=enterEncryptionButtonFunction)    
    #加密文字放置区
    mainTitle.place(x=210,y=0)
    enterLabel.place(x=315,y=170)
    enterButton.place(x=510,y=163)
def decryptTextFunction():
    global enterButton
    print('decryptText')
    decryptImageButton.place_forget()
    decryptTextButton.place_forget()
    buttonDecrypt.place_forget()
    buttonEncryption.place_forget()
    mainTitle=tk.Label(mainWindow,text="请将要解密的文本复制到./File/toFile/toEnc.teXS中\n(这个文件相当于文本文档，直接记事本打开就行)",font=('Arial',14),width=40,height=3)
    enterButton=tk.Button(mainWindow,text="确认",width=5,height=1,command=dencryptTextEnterFunction)
    mainTitle.place(x=210,y=0)
    enterButton.place(x=440,y=230)
def decryptImageFunction():
    print('decryptImage')
    
def encryptionImageFunction():
    print('encryptionImage')
    
def encryptionFunction():
    print('To Encryption')
    global encryptionImageButton,encryptionTextButton
    #加密界面的各种组件
    mainTitle=tk.Label(mainWindow,text="请选择加密文字/图片",font=('Arial',14),width=40,height=3)
    encryptionTextButton=tk.Button(mainWindow,text="加密文字",width=30,height=17,bg='white',command=encryptionTextFunction)
    encryptionImageButton=tk.Button(mainWindow,text="加密图片",width=30,height=17,bg='white',command=encryptionImageFunction)
    #加密界面组件放置区
    mainTitle.place(x=210,y=0)
    encryptionTextButton.place(x=90,y=140)
    encryptionImageButton.place(x=570,y=140)
def decryptFunction():
    global decryptImageButton,decryptTextButton
    print('To Decrypt')
    #解密界面的各种组件
    mainTitle=tk.Label(mainWindow,text="请选择加密文字/图片",font=('Arial',14),width=40,height=3)
    decryptTextButton=tk.Button(mainWindow,text="解密文字",width=30,height=17,bg='white',command=decryptTextFunction)
    decryptImageButton=tk.Button(mainWindow,text="解密图片",width=30,height=17,bg='white',command=decryptImageFunction)
    #解密界面组件放置区
    mainTitle.place(x=210,y=0)
    decryptTextButton.place(x=90,y=140)
    decryptImageButton.place(x=570,y=140)
def main(status):
    if status==0:
        global mainTitle,buttonDecrypt,buttonEncryption
        global mainWindow
        #主窗口
        mainWindow=tk.Tk()
        #窗口标题
        mainWindow.title("一个加密/解密 文字/图片的开源小工具")
        #窗口图标
        mainWindow.iconbitmap('ico.ico')
        #设置窗口宽高
        mainWindow.geometry('900x500')
        #主窗口的各种组件
        mainTitle=tk.Label(mainWindow,text="一款可以加密解密文字图片的开源小工具!",font=('Arial',14),width=40,height=3)
        buttonEncryption=tk.Button(mainWindow,text="加密文字/图片",width=30,height=17,bg='white',command=encryptionFunction)
        buttonDecrypt=tk.Button(mainWindow,text="解密文字/图片",width=30,height=17,bg='white',command=decryptFunction)
        #主窗口组件放置区
        mainTitle.place(x=210,y=0)
        buttonEncryption.place(x=90,y=140)
        buttonDecrypt.place(x=570,y=140)
        #主窗口循环
        mainWindow.mainloop()
    elif status==1:
        deputyLabel.place_forget()
        backButton.place_forget()
        enterLabel.place_forget()
        enterButton.place_forget()
        #主窗口的各种组件
        mainTitle=tk.Label(mainWindow,text="一款可以加密解密文字图片的开源小工具!",font=('Arial',14),width=40,height=3)
        buttonEncryption=tk.Button(mainWindow,text="加密文字/图片",width=30,height=17,bg='white',command=encryptionFunction)
        buttonDecrypt=tk.Button(mainWindow,text="解密文字/图片",width=30,height=17,bg='white',command=decryptFunction)
        #主窗口组件放置区
        mainTitle.place(x=210,y=0)
        buttonEncryption.place(x=90,y=140)
        buttonDecrypt.place(x=570,y=140)
    elif status==2:
        deputyLabel.place_forget()
        backButton.place_forget()
        #主窗口的各种组件
        mainTitle=tk.Label(mainWindow,text="一款可以加密解密文字图片的开源小工具!",font=('Arial',14),width=40,height=3)
        buttonEncryption=tk.Button(mainWindow,text="加密文字/图片",width=30,height=17,bg='white',command=encryptionFunction)
        buttonDecrypt=tk.Button(mainWindow,text="解密文字/图片",width=30,height=17,bg='white',command=decryptFunction)
        #主窗口组件放置区
        mainTitle.place(x=210,y=0)
        buttonEncryption.place(x=90,y=140)
        buttonDecrypt.place(x=570,y=140)
main(0)