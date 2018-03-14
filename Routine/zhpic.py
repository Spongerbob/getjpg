#-*- coding:UTF-8 -*-

import re
import os
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    return html

def getpic(html):
    reg = r'src=".+?\.jpg"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)

    imgurllist = []
    for imgurl in imglist:
        src = re.compile(r'com(\/.+?\.jpg)')
        imgsrc = re.findall(src, imgurl)
        imgurllist.append("http://pic1.zhimg.com" + imgsrc[0])

    x = 0
    for i in range(len(imgurllist)):

        path = os.path.abspath('.')
        if i % 3 == 1:
            urllib.request.urlretrieve(imgurllist[i], path + '/zhihu/%s.jpg' % x)

        x += 1

    return imgurllist

html = getHtml("https://www.zhihu.com/question/59136991/answer/177800805")
imgurllist = getpic(html)

print(imgurllist)
