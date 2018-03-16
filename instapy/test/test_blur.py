#Copyright 2018 Indiana Nikel
#Licensed under the Apache License, Version 2.0 (the "License")
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# March 2018
# This script tests the function from flip.R.

# This script tests blur function of InstaPy package.
# This function blurs an image.
# Input  : An image in .jpg.jpeg.png,.tiff format
# Output : A flipped image in .jpg.jpeg.png,.tiff format

import numpy as np
import skimage.io
import pytest
#from InstaPy import blur

# input color: image 1
input = np.array([[[10, 110, 210], [20, 120, 220], [30, 130, 230], [40, 140, 240], [50, 150, 250]],
                  [[20, 120, 220], [30, 130, 230], [40, 140, 240], [50, 150, 250], [10, 110, 210]],
                  [[30, 130, 230], [40, 140, 240], [50, 150, 250], [10, 110, 210], [20, 120, 220]],
                  [[40, 140, 240], [50, 150, 250], [10, 110, 210], [20, 120, 220], [30, 130, 230]],
                  [[50, 150, 250], [10, 110, 210], [20, 120, 220], [30, 130, 230], [40, 140, 240]]],
                 dtype="uint8")

skimage.io.imsave("input.png", input)

# expected output: blur image 1
exp_output = np.array([[[30, 130, 230], [34, 134, 234], [33, 133, 233]],
                       [[34, 134, 234], [33, 133, 233], [27, 127, 227]],
                       [[33, 133, 233], [27, 127, 227], [26, 126, 226]]],
                    dtype="uint8")

#Check if image is blurred correctly

#Blur
def test_blur1(img):
    blur("input.png")
    output = skimage.io.imread("blur.png")
    assert output == exp_output, "The blur function does not work properly"

#In case the intensity values are not in range of 0-255

def test_blur2(img):
    assert np.max(input1) < 255, "Intensity values are incorrect"

def test_blur3(img):
    assert np.max(input1) >=0 , "Intensity values are incorrect"
