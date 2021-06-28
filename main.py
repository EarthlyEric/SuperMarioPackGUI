import os
from  tkinter import* 

win = Tk() # 主視窗建立

win.title("SuperMarioBros Runtime GUI") #主視窗名稱
win.geometry("640x480") #寬x高,視窗大小,預設
win.resizable(False,False)#固定視窗大小
win.iconbitmap("res\Super_Mario_Bros_Pack_GUI_Icon.ico") #視窗圖示
win.config(background="skyblue")
win.mainloop() #常駐

brunsmb1 = Button(text="Run")
brunsmb1.config(background="")
brunsmb1.config(width=10,height=2)
brunsmb1.pack()

