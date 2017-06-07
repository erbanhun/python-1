#-*- coding:utf-8 -*-

import os
import os.path
import PIL
from PIL import Image
import glob, os

rootdir = "F:\python\photo"

def dealPhoto(dir, pixel): # http://pillow.readthedocs.io/en/latest/reference/Image.html
    os.chdir(dir)
    #size = 128, 128
    for infile in glob.glob("*，jpg"): # 只对jpg 有效
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(pixel)
        im.save(file + "_thumbnail.jpg", "JPEG")


def openPhoto_auto(rootdir):
    #parent, dirnames, filenames = os.walk(rootdir)
    #print (parent)
    #dealPhoto(parent)
    for parent, dirnames, filenames in os.walk(rootdir):
        print (parent)
    #for dirname in dirnames:
    #    print ("parent is: " + parent)
    #    print ("dirname is: " + dirname)
        #print('=========================')
        #print(filenames)
        #for filename in filenames:
        #    print ("parent is: " + parent)
        #    print ("filename is:" + filename)
        #    dealPhoto(parent, filename)


if __name__ == "__main__":
    rootdir = "f:/python/photo" # 设图路径
    pixel = (1136, 640) # 设像素
    dealPhoto(rootdir, pixel)
