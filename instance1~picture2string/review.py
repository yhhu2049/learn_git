# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:25:32 2018

this code is to review of instance1

@author: hyh
"""

from PIL import Image
filepath = 'D:/HelloWorld/learngit/instance1~picture2string/Xi.jpg'
outputpath = 'D:/HelloWorld/learngit/instance1~picture2string/Xi2.txt'
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha = 256):
    length = len(ascii_char)
    # 将RGB转换为灰度
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # gray / 256 = ? / length
    unit = length / alpha
    return ascii_char[int(gray*unit)]
if __name__ == '__main__':
    im = Image.open(filepath)
    width = int(im.size[0] / 10)
    height = int(im.size[1] / 20)
    im = im.resize((width,height),Image.NEAREST)
    txt = ''
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
with open(outputpath,'w') as j:
    j.write(txt)