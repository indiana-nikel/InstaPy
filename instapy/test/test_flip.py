#Copyright 2018 Tarini Bhatnagar
#Licensed under the Apache License, Version 2.0 (the "License")
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# March 2018
# This script tests the function from flip.R.

# This script tests flip function of InstaPy package. 
# This function flips an image. It takes an argument for direction from the user: horizontal or vertical.
# Input  : An image in .jpg.jpeg.png,.tiff format
# Output : A flipped image in .jpg.jpeg.png,.tiff format

import numpy as np
import matplotlib.pyplot as plt
import pytest
#from InstaPy import flip

#Define test image for horizontal flip

img_horiz = np.array([[[255,  0,  0 ], [255,  0,  0 ], [255,  0,  0 ]],
                      [[255, 255,255], [255, 255,255], [255, 255,255]],
                      [[255,  0,  0 ], [255,  0,  0 ], [255,  0,  0 ]]], dtype = "uint8")

                
#Define test image for vertical flip

img_vert =  np.array([[[255, 255, 255 ], [255, 255, 255  ], [255, 255, 255  ]],
                      [[ 0 , 255,  0  ], [  0 , 255,  0  ], [  0 , 255,  0  ]],
                      [[ 0 , 255,  0  ], [  0 , 255,  0  ], [  0 , 255,  0  ]]], dtype = "uint8")



#Expected image matrix for horizontal flip

img_horiz_exp = np.array([[[0,  0,   255], [0, 0,  255  ], [0,  0,  255  ]],
                          [[255, 255,255], [255, 255,255], [255, 255,255]],
                          [[0,  0,   255], [0,  0,  255 ], [0,  0,  255 ]]], dtype = "uint8")
 
                
#Expected image matrix for vertical flip

img_vert_exp =  np.array([[[0   , 255,  0   ], [  0 , 255,  0  ], [  0 , 255,  0 ]],
                          [[0   , 255,  0   ], [  0 , 255,  0  ], [  0 , 255,  0  ]],
                          [[255 , 255,  255 ], [255 , 255, 255 ], [ 255 ,255, 255  ]]], dtype = "uint8")
                          
                          
                          
#Saving test images
plt.imsave("img_horiz.png",img_horiz)
plt.imsave("img_vert.png",img_vert)


#Check if image is flipped correctly

#Horizontal flip
def test_flip1():
    flip("img_horiz.png", "h")
    output = plt.imread("flipped.png")[:, :, :3]
    assert (output == img_horiz_exp).all(), "The flip function does not work properly"
    
#plt.imsave("./test_img/img_vert.jpg",img_vert)

#Vertical flip
def test_flip2():
    flip("img_vert.png", "v")
    output = plt.imread("flipped.png")[:, :, :3]
    assert (output == img_vert_exp).all(), "The flip function does not work properly"
    
#Test for argument validity: In case the flip direction is not one of the accepted arguments
def test_flip3():
    assert direction in ["h","v"]   , "Incorrect flip direction"