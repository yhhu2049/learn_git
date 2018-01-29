# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:38:26 2018

this code is for translate picture to "string picture"
based on code of https://www.shiyanlou.com/courses/370

@author: hyh
"""

from PIL import Image
import os
# 输入需要转换的图片名称，包括后缀名
filename = 'Xi.jpg'
# 输入图片缩放比例
f1 = 10
f2 = 20
# no need to be modified below
readpath = 'D:/HelloWorld/learngit/picture fundamental/' + filename
outputpath = 'D:/HelloWorld/learngit/picture fundamental/output.txt'
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(readpath)
    WIDTH = int(im.size[0] / f1)
    HEIGHT = int(im.size[1] / f2)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
#    print(WIDTH , HEIGHT)
    if os.path.exists(outputpath):
        print('old one has been deleted successfully!')
        os.remove(outputpath)
    with open(outputpath,'w') as f:
        f.write(txt)
