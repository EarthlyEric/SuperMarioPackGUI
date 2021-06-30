import lang_loader as lang
import button_lib as bt
import lib
import webbrowser
from  tkinter import*
import json

mainwin = Tk() # 主視窗建立

bg = PhotoImage(file = "res\mainwin_bg_img.png")

canvas_mainwin = Canvas( mainwin, width = 640,height = 360)
canvas_mainwin.pack(fill = "both", expand = True)
canvas_mainwin.create_image( 0, 0, image = bg, anchor = "nw")

mainwin.title(f"{lang.mainwin_title_lang}") #主視窗名稱
mainwin.geometry("1280x720") #寬x高,視窗大小,預設
mainwin.resizable(False,False)#固定視窗大小
mainwin.iconbitmap("res\Super_Mario_Bros_Pack_GUI_Icon.ico") #視窗圖示
mainwin.config(background="skyblue")

b_run_smb1 = Button(text=f"{lang.b_run_smb1_lang}",background="red",width=7,height=2,command=bt.b_run_smb1_run)
b_run_smb1_canvas = canvas_mainwin.create_window(100, 10, anchor = "nw",window = b_run_smb1)

b_run_go_github_img = PhotoImage(file="res\GitHub_Mark.png")
b_run_go_github = Button(background="#39C7AD",image=b_run_go_github_img,command=bt.b_run_go_github)
b_run_go_github_canvas = canvas_mainwin.create_window(0,685,anchor="nw",window=b_run_go_github)

b_run_go_reload_dev_img = PhotoImage(file="res\Reload_Dev_Mark.png")
b_run_go_reload_dev = Button(background="#39C7AD",image=b_run_go_reload_dev_img,command=bt.b_run_go_reload_dev)
b_run_go_reload_dev_canvas = canvas_mainwin.create_window(35,685,anchor="nw",window=b_run_go_reload_dev)

mainwin.mainloop() #常駐#END