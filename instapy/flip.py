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
    Input: string of path for an image file in .jpg, .jpeg, .png, .tiff format
    Output: an image file in .jpg, .jpeg, .png, .tiff format
    '''
    
    #Reading image file as matrix
     input_mat = skimage.io.imread(img)
    
    #Loop for direction to be either horizontal or vertical
    
    #Vertical Flip
    if direction == "v":
        asc=range(0, input_mat.shape[0])
        desc=list(reversed(asc))
        output_mat = input_mat.copy()
        output_mat[asc] = input_mat[desc]

    #Horizontal Flip
    elif direction == "h":
        dim1=input_mat.shape[0]
        dim2=input_mat.shape[1]
        output_mat=np.zeros((dim1,dim2,3))
        for x in range(0,input_mat.shape[0]):
            output_mat[x]=input_mat[x][::-1]
        
    #Converting data type
    output_mat=np.array(output_mat, dtype=np.uint8)

    #Display flipped image to user
    skimage.io.imshow(output_mat)
    #Save flipped image in current folder
    output_path=os.path.splitext(img)[0] +'_flip' + os.path.splitext(img)[1]
    plt.imsave(output_path,output_mat)