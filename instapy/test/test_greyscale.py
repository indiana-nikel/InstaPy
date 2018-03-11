# Copyright 2018 Xin (Alex) Guo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.


# This script tests the greyscale() function.

# greyscale(input_path, output_path) converts a color image into greyscale
# Input: input_path: string, path for the input image file
#        output_path: string, path for the output image file
# Output: an image file at the specified output path


import numpy as np
import matplotlib.pyplot as plt
import pytest
from InstaPy import greyscale

# test_img1: color image
test_img1 = np.array([[[ 10,  20,  40], [ 20,  40,  10], [ 40,  10,  20]],
                      [[ 40,  80, 160], [ 80, 160,  40], [160,  40,  80]],
                      [[ 60, 120, 240], [120, 240,  60], [240,  60, 120]]], dtype = "uint8")

# test_img1_gs: expected greyscale image
test_img1_gs = np.array([[[ 19,  19,  19], [ 31,  31,  31], [ 20,  20,  20]],
                         [[ 77,  77,  77], [123, 123, 123], [ 80,  80,  80]],
                         [[115, 115, 115], [184, 184, 184], [121, 121, 121]]], dtype = "uint8")

plt.imsave("./test_img/test_img1.jpg", test_img1)

# test if the greyscale function works properly
def test_greyscale1():
    greyscale("./test_img/test_img1.jpg", "./test_img/test_img1_gs.jpg")
    output = plt.imread("./test_img/test_img1_gs.jpg")[:, :, :3]
    assert (output == test_img1_gs).all(), "The greyscale function does not work properly."

# test_img2: greyscale image
test_img2 = np.array([[[ 19,  19,  19], [ 31,  31,  31], [ 20,  20,  20]],
                      [[ 77,  77,  77], [123, 123, 123], [ 80,  80,  80]],
                      [[115, 115, 115], [184, 184, 184], [121, 121, 121]]], dtype = "uint8")

plt.imsave("./test_img/test_img2.jpg", test_img2)

# test if the greyscale function changes a greyscale image
def test_greyscale2():
    greyscale("./test_img/test_img2.jpg", "./test_img/test_img2_gs.jpg")
    output = plt.imread("./test_img/test_img2_gs.jpg")[:, :, :3]
    assert (output == test_img2).all(), "The greyscale function should not change a greyscale image."

# test of exception handling for milestone 3, not required in this milestone    
def test_non_string_input():
    with pytest.raises(TypeError):
        greyscale(123, "./test_img/test_img1_gs.jpg")

def test_nonexistent_input_path():
    with pytest.raises(FileNotFoundError):
        greyscale("./123/456.jpg", "./test_img/test_img1_gs.jpg")

def test_non_image_input_file():
    with pytest.raises(OSError):
        greyscale("./test_img/test.pdf", "./test_img/test_img1_gs.jpg")

def test_non_string_output():
    with pytest.raises(TypeError):
        greyscale("./test_img/test_img1.jpg", 123)

def test_nonexistent_output_path():
    with pytest.raises(FileNotFoundError):
        greyscale("./test_img/test_img1.jpg", "./123/456.jpg")
