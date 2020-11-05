#!/usr/bin/python3
from PIL import Image
import os
import pathlib



print("Start scaling picture...")

maxSize = (1920, 1080)
path = os.getcwd()
car = path.split()[-1]
#sufix = path.split()[-1]

i = 1
fileList = os.listdir(path)
for fileName in fileList:
    print(fileName)
    
    if(os.path.isdir(fileName)):
        os.chdir(fileName)
        imageList = os.listdir(os.getcwd())
        print(fileName, " - is a dir")
    else:
        print(fileName, " - is not a dir")
        continue
    
    for imageName in imageList:
        print(imageName)
        os.chdir('../')
        # inputPath = os.path.join(path, dirName, imageName)
        # newName = car + "_" + str(i) + ".JPG"
        # i+=1
        # outputPath = os.path.join(path, newName)
        # print("input = ", inputPath)
        # print("output = ", outputPath)
        # image = Image.open(inputPath)
        # image.thumbnail(maxSize, Image.ANTIALIAS)
        # image.save(outputPath)