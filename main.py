from  tkinter import*
import lib,webbrowser,json,button_lib as bt,lang_loader as lang,winsound
from tkinter import ttk

mainwin = Tk() # 主視窗建立

bg = PhotoImage(file = "res\mainwin_bg_img.png")
canvas_mainwin = Canvas( mainwin, width = 640,height = 360)
canvas_mainwin.pack(fill = "both", expand = True)
canvas_mainwin.create_image( 0, 0, image = bg, anchor = "nw")

mainwin.title(f"{lang.mainwin_title_lang}") #主視窗名稱
mainwin.geometry("1280x720") #寬x高,視窗大小,預設
mainwin.resizable(False,False)#固定視窗大小
mainwin.iconbitmap("res\Super_Mario_Bros_Pack_GUI_Icon.ico") #視窗圖示

b_run_smb1 = Button(text=f"{lang.b_run_smb1_lang}",background="red",relief=RAISED,width=7,height=2,command=bt.b_run_smb1_run)
b_run_smb1_canvas = canvas_mainwin.create_window(180,205,anchor="nw",window = b_run_smb1)

b_run_sm2 = Button(text=f"{lang.b_run_smb2_lang}",background="red",relief=RAISED,width=7,height=2,command=bt.b_run_smb2_run)
b_run_smb2_canvas = canvas_mainwin.create_window(605,205,anchor="nw",window = b_run_sm2)

b_run_sm3 = Button(text=f"{lang.b_run_smb3_lang}",background="red",relief=RAISED,width=7,height=2,command=bt.b_run_smb3_run)
b_run_sm3_canvas = canvas_mainwin.create_window(1030,205,anchor="nw",window = b_run_sm3)

def b_run_settings_os():
    settings = Toplevel(mainwin)
    settings.title("Settings")
    settings.geometry("300x450")

    with open("config\config.json") as lang_get:
            lang_get_load_temp = json.load(lang_get)
            lang_get_load = lang_get_load_temp["lang"]

    settings.resizable(False,False)
    lang_combo = ttk.Combobox(settings,values=["English","繁體中文"])

    lang_combo.grid(column=0, row=1)#設語言id
    if lang_get_load == "zh_tw":
        pass
    elif lang_get_load =="en_us":
        pass
    lang_combo.current(0)#預設語言id
    print(lang_combo.get())#選擇語言結果名
    print(lang_combo.current())#選擇語言結果id
    lang_switch = lang_combo.current()
    
    
    if lang_switch == 0:
        with open("config\config.json") as lang_change:
            lang_change_load = lang_change["lang"]
    elif lang_switch == 1:
        print("完成")
             

b_run_settings_img = PhotoImage(file="res\Settings_icon.png")
b_run_settings = Button(background="white",image=b_run_settings_img,relief=RAISED,command=b_run_settings_os)
b_run_setting_canvas = canvas_mainwin.create_window(1248,46,anchor="nw",window=b_run_settings)

b_run_exit_img = PhotoImage(file="res\Exit_icon.png")
b_run_exit = Button(background="white",image=b_run_exit_img,relief=RAISED,command=mainwin.destroy)
b_run_exit_canvas = canvas_mainwin.create_window(1248,80,anchor="nw",window=b_run_exit)

b_run_go_github_img = PhotoImage(file="res\GitHub_Mark.png")
b_run_go_github = Button(background="#39C7AD",image=b_run_go_github_img,relief=RAISED,command=bt.b_run_go_github)
b_run_go_github_canvas = canvas_mainwin.create_window(0,685,anchor="nw",window=b_run_go_github)

b_run_go_reload_dev_img = PhotoImage(file="res\Reload_Dev_Mark.png")
b_run_go_reload_dev = Button(background="#39C7AD",image=b_run_go_reload_dev_img,relief=RAISED,command=bt.b_run_go_reload_dev)
b_run_go_reload_dev_canvas = canvas_mainwin.create_window(35,685,anchor="nw",window=b_run_go_reload_dev)

mainwin.mainloop() #常駐#END