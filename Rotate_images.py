# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:41:15 2021
this script treats all not hidden images in a directory
treatmens is 
Torate 90 counter clock 
resize to 128 x 128 pixels
elimiante alpah channel

@author: LuisMiguel
"""

import os
from  PIL import Image as im
counter=0
my_directory = os.path.abspath(".")  #to know where we are

#path creation to directories with original images and destination
dir_original_images = os.path.join(my_directory, "images\\original")
dir_rotated_images = os.path.join(my_directory,"images\\rotated")

print()
print("I start adjusting Images")
print("========================")

#for all files listed in the directory of original images
for f in os.listdir(dir_original_images):
    if not f.startswith("."): #except for hidden files
        print(f)
        image_file = os.path.join(dir_original_images,f)
        rotated_image_file = os.path.join(dir_rotated_images,f)
        image_to_rotate = im.open(image_file)
        rotated_image = image_to_rotate.rotate(90)
        #we need to remove alpha channel of formal "LA" cause it is not
        #supported by JPEG format
        resized_image = rotated_image.resize((128,128)).convert("L")
        resized_image.save(rotated_image_file,format='PNG')
        counter +=1

print("========================")
print("{} images adjusted".format(counter))