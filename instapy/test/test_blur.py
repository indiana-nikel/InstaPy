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
from scipy.ndimage.filters import convolve
import skimage.io
import matplotlib.pyplot as plt
import sys
import pytest
from InstaPy import blur

# input color: image 1
input1 = np.array([[[10, 20, 30, 40, 50],
                    [20, 30, 40, 50, 10],
                    [30, 40, 50, 10, 20],
                    [40, 50, 10, 20, 30],
                    [50, 10, 20, 30, 40]],   #R values
                   [[110, 120, 130, 140, 150],
                    [120, 130, 140, 150, 110],
                    [130, 140, 150, 110, 120],
                    [140, 150, 110, 120, 130],
                    [150, 110, 120, 130, 140]],   #G values
                   [[210, 220, 230, 240, 250],
                    [220, 230, 240, 250, 210],
                    [230, 240, 250, 210, 220],
                    [240, 250, 210, 220, 230],
                    [250, 210, 220, 230, 240]]   #B values
                   ])

skimage.io.imsave("./test_img/blur/input1.jpg", input1)

# expected output: blur image 1
exp_output1 = np.array([[[30, 34.4444, 33.3333],
                         [34.4444, 33.3333, 26.6666],
                         [33.3333, 26.6666, 25.5555]],  #R values
                        [[130, 134.4444, 133.3333],
                         [134.4444, 133.3333, 126.6666],
                         [133.3333, 126.6666, 125.5555]],  #G values
                        [[230, 234.4444, 233.3333],
                         [234.4444, 233.3333, 226.6666],
                         [233.3333, 226.6666, 225.5555]]   #B values
                        ])

#Check if image is blurred correctly

#Blur
def test_blur1(img):
    blur("./test_img/blur/input1.jpg")
    output = skimage.io.imread("blur.jpg")
    assert output == exp_output1, "The blur function does not work properly"

#In case the intensity values are not in range of 0-255

def test_blur2(img):
    assert np.max(input1) < 255, "Intensity values are incorrect"

def test_blur3(img):
    assert np.max(input1) >=0 , "Intensity values are incorrect"
