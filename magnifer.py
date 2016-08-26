#!python
from __future__ import print_function
from PIL import Image
import numpy as np


dir = input("Image you want scale: ")
try:
    im = Image.open(dir)
except :
    exit()
try:
    scale = int(input("Set the scale you want: "))
except TypeError:
    exit()

print(im.format,im.size,im.mode)
width,height = im.size;
pix = im.load()

p = np.array(im)

newim = Image.new("RGB",(width*scale,height*scale));


#print("psize ",p.size,'-->',p[0].size)
for i in range(0 , width):
        for j in range(0,height):

            for x in range(scale):
                for y in range(scale):
                    cell = p[i][j]
                    r = p[i][j]
                    b = p[i][j]
                    rb = p[i][j]

                    if i + 1< width:
                        r = p[i+1][j]
                    if j + 1 < height:
                        b = p[i][j+1]
                    if i + 1 < width and j + 1 < height:
                        rb = p[i+1][j+1]

                    tmp1 = tmp2 = tmp3 = cell;

                    for k in range(3):
                        tmp1[k] = ((scale - x)*int(cell[k]) + x * int(r[k])) / scale
                        tmp2[k] = ((scale - y) * int(cell[k]) + y * int(b[k])) / scale
                        tmp3[k] = ((scale - x) * int(cell[k]) + x * int(rb[k]) + (scale - y) * int(cell[k]) + y * int(rb[k])) / (2 * scale)
                        cell[k] = int(tmp1[k]/3+tmp2[k]/3+tmp3[k]/3)

                    try:
                        newim.putpixel(((j*scale + y),(i*scale + x)),(int(cell[0]),int(cell[1]),int(cell[2])))
                    except IndexError:
                        print("error",i,j)

dir = dir[:dir.rfind('.')]
dir += "_"+str(scale)+"x"
dir += ".png";
newim.save(dir,"PNG")
newim.show()
im.show()
