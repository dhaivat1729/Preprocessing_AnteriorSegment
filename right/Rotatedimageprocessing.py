# this program will take cow images as input and will process blobs after rotating it.

from SimpleCV import *
import os
import time

input_image_global_path = "/home/dhaivat666/Left/left_45_first__"
save_path = "/home/dhaivat666/Left/Rotated_images/"


for i in range(0,162):
    input_path = input_image_global_path + str(i) + ".png"
    img = Image(input_path)
    img = img.rotate90()
    blobs = img.findBlobs()
    for b in blobs:
        if b.area() > 50 and b.area() < 1200:
            if (b.coordinates()[0] > 436 and b.coordinates()[0] < 583) and (b.coordinates()[1] > 498 and b.coordinates()[1] < 691):
                b.draw(Color.BLACK,15)
                b.drawHull(Color.BLACK)
    save = save_path + str(i) + ".png"
    img.save(save)
