# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:41:15 2021

@author: LuisMiguel
"""

import os
from  PIL import Image as im
my_directory = os.path.abspath(".")
dir_original_images = os.path.join(my_directory, "images\\original")
dir_rotated_images = os.path.join(my_directory,"images\\rotated")
for f in os.listdir(dir_original_images):
    image_file = os.path.join(dir_original_images,f)
    rotated_image_file = os.path.join(dir_rotated_images,f)
    image_to_rotate = im.open(image_file)
    rotated_image = image_to_rotate.rotate(90)
    rotated_image.save(rotated_image_file)
    print(image_file)