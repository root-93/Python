#!/usr/bin/python3
from PIL import Image
import os
import pathlib

print("Start scaling picture...")
mainPath = os.getcwd()
car = mainPath.split('/')[-1]
maxSize = (1920, 1080)

def removeOld():   
    for fileName in os.listdir(mainPath):
        localPath = os.path.join(mainPath,fileName)
        if(os.path.isdir(localPath)):
            os.chdir(localPath)
        else:
            continue
        for imageName in os.listdir(os.getcwd()):
            if car in imageName:
                os.remove(imageName)
        os.chdir(mainPath)


def scaleImages():
    i = 1
    for fileName in os.listdir(mainPath):
        localPath = os.path.join(mainPath,fileName)

        if(os.path.isdir(localPath)):
            os.chdir(localPath)
        else:
            continue
        
        for imageName in os.listdir(os.getcwd()):
            inputPath = os.path.join(localPath, imageName)
            newName =car + "_" + fileName + "_" + str(i) + ".JPG"
            i+=1
            outputPath = os.path.join(localPath, newName)
            print("input = ", inputPath)
            print("output = ", outputPath)
            image = Image.open(inputPath)
            image.thumbnail(maxSize, Image.ANTIALIAS)
            image.save(outputPath)
        
        i = 1
        os.chdir(mainPath)


#def makeSlideShowImages():
    # soon...

#---- main function ----------------

removeOld()
scaleImages()
#makeSlideShowImages()