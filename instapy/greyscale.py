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

import numpy as np
import matplotlib.pyplot as plt

def greyscale(input_path, output_path):
    '''
    Convert a color image into greyscale
    Input: input_path: string, path for the input image file
           output_path: string, path for the output image file
    Output: an image file at the specified output path
    '''
    # exception handling for milestone 3, not required in this milestone
    try:
        img = plt.imread(input_path)
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

    height = img.shape[0]
    width = img.shape[1]

    img_gs = np.zeros(img.shape, dtype = "uint8")

    for i in range(height):
        for j in range(width):
            R = img[i][j][0]
            G = img[i][j][1]
            B = img[i][j][2]

            grey = round(0.3*R + 0.59*G + 0.11*B)

            img_gs[i][j][0] = grey
            img_gs[i][j][1] = grey
            img_gs[i][j][2] = grey

    # exception handling for milestone 3, not required in this milestone
    try:
        plt.imsave(output_path, img_gs)
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
