#-------------------------------------------------------------------------------
# Name:        squares
# Purpose:		Transform an image by chipping it into randomly rotated squares
#
# Author:      Christian Schlosser
#
# Created:     21/03/2016
# Copyright:   (c) The Idea Plant LTD 2016
# Licence:     MIT
#-------------------------------------------------------------------------------

from PIL import Image, ImageOps
import subprocess, sys, os, glob
import random

#filename = 'test.png'
#square_size = 300
filename = input('file:')
square_size = input('Square size :(integer)')
square_size = int(square_size)

im = Image.open(filename)
pix = im.load()
width, height = im.size



print('size x, y:', width, height)



region_x = 0;
region_y=0;
rotations = [0,90,180,270]

while (region_x+square_size < width) :
    region_y=0
    while (region_y +square_size< height):
        #print('regx, regy, modx, mody',region_x, region_y, (region_x+square_size)%square_size, (region_y+square_size)%square_size)
        end_x =min(region_x+square_size,width)
        end_y =min(region_y+square_size,height)
        box= (region_x,region_y,end_x,end_y)  #(left, upper, right, lower) where 0,0 is upper left
        #print(min(region_x+square_size,width),min(region_y+square_size,height))
        #print('box size',end_x-region_x, end_y-region_y)
        region = im.crop(box)

        #region = region.transpose(Image.ROTATE_90)
        region = region.rotate(random.choice(rotations))

        region_y += square_size
        im.paste(region, box)

    region_x+=square_size





im.save('modified_'+str(square_size)+'_'+filename)