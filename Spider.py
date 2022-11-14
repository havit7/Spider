#Author: Javier Rodríguez.      .havit7.
import requests
import re
import os
from bs4 import BeautifulSoup

url1 = "https://www.malaga.eu"
response = requests.get(url1)
html = BeautifulSoup(response.text, 'html.parser')
z = 0
patt = re.compile('src="(.*?)"')
for a in html.find_all('img'):
    url = re.findall(patt, str(a))[0]
    if "http" not in url:
        url = url1 + url
    imagen = requests.get(url).content
    print("_______________________")
    try:
        if "jpg" in url:
            with open("$pIdeR" + str(z) + ".jpg", "wb") as printed:
                printed.write(imagen)
                print("Dowloaded $pIdeR jpg " + str(z))
        if "png" in url:
            with open("$pIdeR" + str(z) + ".png", "wb") as printed:
                printed.write(imagen)
                print("Dowloaded $pIdeR png " + str(z))
        if "bmp" in url:
            with open("$pIdeR" + str(z) + ".bmp", "wb") as printed:
                printed.write(imagen)
                print("Dowloaded $pIdeR bmp " + str(z))
        if "gif" in url:
            with open("$pIdeR" + str(z) + ".gif", "wb") as printed:
                printed.write(imagen)
                print("Dowloaded $pIdeR gif " + str(z))
        if "jpeg" in url:
            with open("$pIdeR" + str(z) + ".jpeg", "wb") as printed:
                printed.write(imagen)
                print("Dowloaded $pIdeR jpeg " + str(z))
        if "webp" in url:
            with open("$pIdeR" + str(z) + ".webp", "wb") as printed:
                printed.write(imagen)
                print("Dowloaded $pIdeR webp " + str(z))
        z += 1
    except:
        print(url)
