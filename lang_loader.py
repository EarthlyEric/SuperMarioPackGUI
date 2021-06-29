import json

#導入設定文件
with open("config\config.json", "r",encoding = "utf8") as config:
   data = json.load(config)
   lang = data["lang"]

#導入語言文件
if lang=="zh_tw":
  with open("lang\zh_tw.json", "r",encoding = "utf8") as lang_id:#載入語言文件(Taiwan)
   temp = json.load(lang_id)
   b_run_smb1_lang = temp["b_run_smb1_lang"]
   mainwin_title_lang = temp["mainwin_title_lang"]
elif lang =="en_us":
 with open("lang\en_us.json", "r",encoding = "utf8") as lang_id:#載入語言文件(Engliah_USA)
   temp = json.load(lang_id)
   b_run_smb1_lang = temp["b_run_smb1_lang"]
   mainwin_title_lang = temp["mainwin_title_lang"]