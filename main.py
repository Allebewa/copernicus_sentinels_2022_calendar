import ctypes
import requests
import datetime

dt = datetime.datetime.today()

response = requests.get("https://esamultimedia.esa.int/img/2021/12/2022_Sentinels_digital_calendar_1024x768_211215"+ str(dt.month) +".jpg")
file = open("PATH_TO_PICTURES\\esa_background_"+ str(dt.month) +"_"+ str(dt.year) +".jpg", "wb")
file.write(response.content)
file.close()

image_path = file.name
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
