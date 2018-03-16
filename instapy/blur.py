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

def blur(input_path, output_path):
    '''
    Blurs an image
    Input: string of path for an image file in .png format
    Output: an image file in .png format
    '''
    try:
        input_img = skimage.io.imread(input_path)
    except AttributeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except TypeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except FileNotFoundError:
        print("The input file/path does not exist.")
        raise
    except OSError:
        print("The input file is not an image.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise

    output_img = np.ones((len(input_img)-2, len(input_img[0])-2, 3), dtype="uint8")

    for i in range(1,len(input_img)-1):
        for j in range(1,len(input_img[i])-1):
            for k in range(0, len(input_img[i][j])):
                tl = np.array(input_img[i+1][j-1][k], dtype="uint64")
                tm = np.array(input_img[i+1][j][k], dtype="uint64")
                tr = np.array(input_img[i+1][j+1][k], dtype="uint64")
                cl = np.array(input_img[i][j-1][k], dtype="uint64")
                cm = np.array(input_img[i][j][k], dtype="uint64")
                cr = np.array(input_img[i][j+1][k], dtype="uint64")
                bl = np.array(input_img[i-1][j-1][k], dtype="uint64")
                bm = np.array(input_img[i-1][j][k], dtype="uint64")
                br = np.array(input_img[i-1][j+1][k], dtype="uint64")
                new_pix = np.round((1/9)*(tl+tm+tr+cl+cm+cr+bl+bm+br))
                output_img[i-1][j-1][k] = new_pix

    try:
        skimage.io.imsave(output_path, output_img)
    except AttributeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except TypeError:
        print("Please provide a string as the path for the output image file.")
        raise
    except FileNotFoundError:
        print("The output path does not exist.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise
