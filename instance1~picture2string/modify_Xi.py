# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:38:26 2018
f
@author: hyh
"""


# =============================================================================
# from PIL import Image
# import argparse
# 
# #命令行输入参数处理
# parser = argparse.ArgumentParser()
# 
# parser.add_argument('file')     #输入文件
# parser.add_argument('-o', '--output')   #输出文件
# parser.add_argument('--width', type = int, default = 80) #输出字符画宽
# parser.add_argument('--height', type = int, default = 80) #输出字符画高
# 
# #获取参数
# args = parser.parse_args()
# 
# IMG = args.file
# WIDTH = args.width
# HEIGHT = args.height
# OUTPUT = args.output
# 
# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 
# # 将256灰度映射到70个字符上
# def get_char(r,g,b,alpha = 256):
#     if alpha == 0:
#         return ' '
#     length = len(ascii_char)
#     gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
# 
#     unit = (256.0 + 1)/length
#     return ascii_char[int(gray/unit)]
# 
# if __name__ == '__main__':
# 
#     im = Image.open(IMG)
#     im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
# 
#     txt = ""
# 
#     for i in range(HEIGHT):
#         for j in range(WIDTH):
#             txt += get_char(*im.getpixel((j,i)))
#         txt += '\n'
# 
#     print (txt)
# 
#     #字符画输出到文件
#     if OUTPUT:
#         with open(OUTPUT,'w') as f:
#             f.write(txt)
#     else:
#         with open("output.txt",'w') as f:
#             f.write(txt)
# =============================================================================



# =============================================================================
# from PIL import ImageColor
# print(ImageColor.getcolor('red', 'RGBA'))
# # 也可以只以RBG的方式查看
# print(ImageColor.getcolor('blue', 'RGB'))
# =============================================================================
        
# =============================================================================
from PIL import Image
 
im_path = r'D:/HelloWorld/learngit/picture fundamental/Xi.jpg'
im = Image.open(im_path)
width, height = im.size
 # 宽高
print(im.size, width, height)
 # 格式，以及格式的详细描述
print(im.format, im.format_description)
# crop
croped_im = im.crop((30, 0, 700, 850))
# copy
copied_im = im.copy()
# paste
copied_im.paste(croped_im,(0,0))
# save
save_path = r'D:/HelloWorld/learngit/picture fundamental/modified_Xi.jpg'
copied_im.save(save_path)

copied2_im = im.copy()
im2 = copied2_im.resize((500,500),Image.NEAREST)
save_path = r'D:/HelloWorld/learngit/picture fundamental/fat_Xi.jpg'
im2.save(save_path)

#im.paste(croped_im, (0, 0))