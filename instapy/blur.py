# Copyright 2018 Indiana Nikel
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

import numpy as np
import skimage.io
import matplotlib.pyplot as plt

def blur(img):
    '''
    Blurs an image
    Input: string of path for an image file in .jpg, .jpeg, .png, .tiff format
    Output: an image file in .jpg, .jpeg, .png, .tiff format
    '''
    input_img = skimage.io.imread(img)
    output_img = np.ones((len(input_img)-2, len(input_img[0])-2, 3), dtype="uint8")

    for i in range(1,len(input_img)-1):
        for j in range(1,len(input_img[i])-1):
            tl = np.array(input_img[i+1][j-1], dtype="uint64")
            tm = np.array(input_img[i+1][j], dtype="uint64")
            tr = np.array(input_img[i+1][j+1], dtype="uint64")
            cl = np.array(input_img[i][j-1], dtype="uint64")
            cm = np.array(input_img[i][j], dtype="uint64")
            cr = np.array(input_img[i][j+1], dtype="uint64")
            bl = np.array(input_img[i-1][j-1], dtype="uint64")
            bm = np.array(input_img[i-1][j], dtype="uint64")
            br = np.array(input_img[i-1][j+1], dtype="uint64")
            new_pix = np.round((1/9)*(tl+tm+tr+cl+tm+tr+bl+bm+br))
            output_img[i-1][j-1] = new_pix

    skimage.io.imsave("blur.jpg", output_img)
