from PIL import Image,ImageDraw,ImageFont
import glob, os
import time

timer = time.time()

for i in range(0,1):
    im1 = Image.open("b19.png")
    im2 = Image.new('RGBA', (300,90))
    draw = ImageDraw.Draw(im2)
    xy = 0,0
    txt = 'Justplay'
    if len(txt)>28:
        txt = txt[:28]+'\n'+txt[28:]
    if len(txt)>10:
        F = ImageFont.truetype(font="arial.ttf", size=25)
        draw.multiline_text(xy, txt, fill=(0,0,0,250) ,font=F, anchor=None ,direction=None, features=None)
        im2 = im2.rotate(47, expand=True)
        im1.paste(im2,box=(170,600),mask=im2)
    else:
        F = ImageFont.truetype(font="arial.ttf", size=45)
        draw.multiline_text(xy, txt, fill=(0,0,0,250) ,font=F, anchor=None ,direction=None, features=None)
        im2 = im2.rotate(47, expand=True)
        im1.paste(im2,box=(170,600),mask=im2)
    im1.show()



#im1.show()
#im1.save("heww.png", "PNG")
