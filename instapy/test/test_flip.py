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
import pytest
from InstaPy import flip

#Define test image for horizontal flip

img_h=np.array([[255,  0,  0 ],
                [255, 255,255],
                [255,  0,  0 ]
                ])
                
#Define test image for vertical flip

img_v=np.array([[255, 255, 255],
                [ 0 , 255,  0 ],
                [ 0 , 255,  0 ]
                ])
                
#Expected image matrix for horizontal flip

img_h_e=np.array([[ 0 ,  0 , 255],
                  [255, 255, 255],
                  [ 0  , 0 , 255]
                ])
                
#Expected image matrix for vertical flip

img_v_e=np.array([[  0   , 255 ,  0 ],
                  [  0   , 255 ,  0 ],
                  [ 255  , 255 , 255]
                ])
                
#Check if image is flipped correctly

#Horizontal flip
def test_flip1(img, direction):
    assert flip(img_h, direction='h') == img_h_e, "The flip function does not work properly"
    

#Vertical flip
def test_flip2(img, direction):
    assert flip(img_v, direction='v') == img_v_e, "The flip function does not work properly"
    

#In case the flip direction is not one of the accepted arguments

def test_flip3(img, direction):
    assert direction in ["h","v"]   , "Incorrect flip direction"
    

#In case the intensity values are nt in range of 0-255

def test_flip4(img, direction):
    assert np.max(img_h) < 255, "Intensity values are incorrect"
    
def test_flip5(img, direction):
    assert np.max(img_h) >=0 , "Intensity values are incorrect"
    

    
    
