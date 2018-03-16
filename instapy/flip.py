#Copyright 2018 Tarini Bhatnagar
#Licensed under the Apache License, Version 2.0 (the "License")
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# March 2018
# This script is for function flip.

#Package dependencies
import numpy as np
from scipy.ndimage.filters import convolve
import skimage.io
import matplotlib.pyplot as plt
import sys
import os
%matplotlib inline

def flip(img, direction):
    '''
    Flips an image in either horizonatl or vertical direction
    Arguments:
    	img: path of input file
    	direction: direction of flip, horizontal="h", vertical = "v"
    Output: an image file in .png format
    '''
    
    #Reading image file as matrix
    input_mat = plt.imread(img)
    
    #Loop for direction to be either horizontal or vertical
    
    #Vertical Flip
    if direction == "v":
        asc=range(0, input_mat.shape[0])
        desc=list(reversed(asc))
        output_mat = input_mat.copy()
        output_mat[asc] = input_mat[desc]

    #Horizontal Flip
    elif direction == "h":
        elif direction == "h":
        asc=range(0, input_mat.shape[1])
        desc=list(reversed(asc))
        output_mat = input_mat.copy()
        output_mat[:,asc] = input_mat[:,desc]
   
        
    #Converting data type
    output_mat=np.array(output_mat, dtype=np.uint8)

    #Save flipped image 
    plt.imsave("flipped.png",output_mat)