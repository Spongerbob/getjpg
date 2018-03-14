#-*- coding:UTF-8 -*-

import urllib.request
import re
from bs4 import BeautifulSoup

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html

def getWord(html):
    #bs = BeautifulSoup(html, "lxml") #实例化对象
    bs = BeautifulSoup(html, "html.parser") #实例化对象
    namelist = bs.findAll("li")

    return namelist

url = "http://www.lzu.edu.cn/"
html = getHtml(url)
# bs = BeautifulSoup(html, "lxml")
# namelist = bs.findAll("a")

namelist = getWord(html)

for name in namelist:
    print(name.get_text())      #获取a标签中的文字
