##
## Program: Remove reflections from cow EYE images which still have reflections after applying preprocessing algorithm
## Author: Dhaivat Bhatt
## Date: 27/01/2015
##

# necessary packages
from SimpleCV import *
import numpy as np
import cv2
import os

# Extracting path where the script is running
cwd = os.path.dirname(os.path.abspath(__file__))

# Input image to those not processed images
input_path = cwd + '/Final_images/'

# using inpaint method of opencv, removing specular reflections from those images
for j in range(31, 57):
    for i in range(0,5):
        img = Image(input_path + str(j) + '.png')
        img.grayscale().binarize(75).invert().dilate(5).save(cwd + '/Mask.png') # generating mask for inpaint method
        imgOpen = cv2.imread(input_path + str(j) + '.png')
        mask = cv2.imread(cwd + '/Mask.png',0)
        dst = cv2.inpaint(imgOpen, mask, 5, cv2.INPAINT_NS)
        cv2.imwrite(input_path + str(j) + '.png', dst)
