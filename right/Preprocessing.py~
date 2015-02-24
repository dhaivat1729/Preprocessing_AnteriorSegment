##
## Program: Remove reflections from the cow EYE images using blob detection algorithm and then extracting images which have reflections after preprocessing
## Author: Dhaivat Bhatt
## Date: 26/01/2015
##

## Necessary packages

from SimpleCV import *
import os
import time

## Extracting path where the script is running
cwd = os.path.dirname(os.path.abspath(__file__))

## Path of input images
input_image_global_path = cwd + "/raw_images/right_45_first__"

## Saving images after removing reflections
save_path = cwd + "/Final_images/"

## Preprocessed images path
global_path = cwd + "/Final_images/"

## Filtering out those preoprocessed images where reflections exist
global_save_path = cwd + "/Not_processed_images/"

## This loop is to remove reflections from those images
for i in range(0,162):
    input_path = input_image_global_path + str(i) + ".png"
    img = Image(input_path)
    blobs = img.findBlobs()
    for b in blobs:
        if b.area() > 50 and b.area() < 1200:
            if (b.coordinates()[0] > 597 and b.coordinates()[0] < 790) and (b.coordinates()[1] > 436 and b.coordinates()[1] < 583):
                b.draw(Color.BLACK,15)
                b.drawHull(Color.BLACK)
    save = save_path + str(i) + ".png"
    img.save(save)


## Extracting those preprocessed images reflections exist
for i in range(0, 162):
    image_path  = global_path + str(i) + ".png"
    img = Image(image_path)
    imgCropped = img.crop([510, 460, 240, 95])
    imgCroppedmean = imgCropped.meanColor()
    if imgCroppedmean[0] > 15 and imgCroppedmean[1] > 15 and imgCroppedmean[2] > 15:
        save_path = global_save_path + str(i) + ".png"
        img.save(save_path)
