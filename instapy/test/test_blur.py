#Copyright 2018 Indiana Nikel
#Licensed under the Apache License, Version 2.0 (the "License")
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# March 2018
# This script tests the function from flip.R.

# This script tests blur function of InstaPy package.
# This function blurs an image.
# Input  : An image in .pngnformat
# Output : A flipped image in .png format

import numpy as np
import skimage.io
import pytest
from instapy.blur import blur

# input color: image 1
input = np.array([[[10, 110, 210], [20, 120, 220], [30, 130, 230], [40, 140, 240], [50, 150, 250]],
                  [[20, 120, 220], [30, 130, 230], [40, 140, 240], [50, 150, 250], [10, 110, 210]],
                  [[30, 130, 230], [40, 140, 240], [50, 150, 250], [10, 110, 210], [20, 120, 220]],
                  [[40, 140, 240], [50, 150, 250], [10, 110, 210], [20, 120, 220], [30, 130, 230]],
                  [[50, 150, 250], [10, 110, 210], [20, 120, 220], [30, 130, 230], [40, 140, 240]]],
                 dtype="uint8")

skimage.io.imsave("instapy/test/test_img/blur/input.png", input)

# expected output: blur image 1
exp_output = np.array([[[30, 130, 230], [34, 134, 234], [33, 133, 233]],
                       [[34, 134, 234], [33, 133, 233], [27, 127, 227]],
                       [[33, 133, 233], [27, 127, 227], [26, 126, 226]]],
                    dtype="uint8")

skimage.io.imsave("instapy/test/test_img/blur/exp_output.png", exp_output)

#Check if image is blurred correctly

#Blur
def test_blur1():
    blur("instapy/test/test_img/blur/input.png", "instapy/test/test_img/blur/blur.png")
    output = skimage.io.imread("instapy/test/test_img/blur/blur.png")
    test_output = skimage.io.imread("instapy/test/test_img/blur/exp_output.png")
    assert np.array_equal(output, test_output), "The blur function does not work properly"

#Exception Handling
def test_non_string_input():
    with pytest.raises(AttributeError):
        blur(123, "instapy/test/test_img/blur/blur.png")

def test_non_string_output():
    with pytest.raises(AttributeError):
        blur("instapy/test/test_img/blur/input.png", 123)

def test_nonexistent_input_path():
    with pytest.raises(FileNotFoundError):
        blur("./123/456.png", "instapy/test/test_img/blur/blur.png")

def test_nonexistent_output_path():
    with pytest.raises(FileNotFoundError):
        blur("instapy/test/test_img/blur/input.png", "./123/456.jpg")

def test_non_image_input_file():
    with pytest.raises(OSError):
        blur("instapy/test/test_img/blur/test.pdf", "instapy/test/test_img/blur/blur.png")


