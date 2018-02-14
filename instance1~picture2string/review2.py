# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:05:07 2018

@author: hyh
"""

#gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
from PIL import Image
openfile = 'Xi.jpg'
savefile = 'Xi3.txt'
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\(\
|{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,b,g,alpha = 256):
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
#    gray / alpha = x / length
    x = int(length * gray / alpha)
    return ascii_char[x]
if __name__ == '__main__':
    im = Image.open(openfile)
    Wid = int(im.size[0]/10)
    Hei = int(im.size[1]/20)
    im = im.resize((Wid,Hei),Image.NEAREST)
    txt = ''
    for i in range(Hei):
        for j in range(Wid):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
with open(savefile,'w') as j:
    j.write(txt)