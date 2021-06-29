import lang_loader as lang
import button_lib as bt
import lib
from  tkinter import*
import json

mainwin = Tk() # 主視窗建立

bg = PhotoImage(file = "res\mainwin_bg_img.png")

canvas_bg = Canvas( mainwin, width = 640,height = 360)
canvas_bg.pack(fill = "both", expand = True)
canvas_bg.create_image( 0, 0, image = bg, 
                     anchor = "nw")

mainwin.title(f"{lang.mainwin_title_lang}") #主視窗名稱
mainwin.geometry("640x360") #寬x高,視窗大小,預設
mainwin.resizable(False,False)#固定視窗大小
mainwin.iconbitmap("res\Super_Mario_Bros_Pack_GUI_Icon.ico") #視窗圖示
mainwin.config(background="skyblue")

b_run_smb1 = Button(text=f"{lang.b_run_smb1_lang}",background="red",width=7,height=2,command=bt.b_run_smb1_run)
button1_canvas = canvas_bg.create_window( 100, 10, anchor = "nw",window = b_run_smb1)


mainwin.mainloop() #常駐#END