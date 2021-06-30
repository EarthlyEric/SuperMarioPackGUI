from  tkinter import*
import os
import lib
import webbrowser 

def b_run_smb1_run():
 
 os.system("VirtuaNES\VirtuaNES.exe Rom\Super_Mario_Bros.nes")

def b_run_go_github():
    github_url= "https://github.com/EarthlyEric/Super_Mario_Bros_Pack_GUI"
    webbrowser.open(github_url)

def b_run_go_reload_dev():
    reload_dev_url ="https://home.reload-dev.ml/"
    webbrowser.open(reload_dev_url)