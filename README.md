## InstaPy

![](img/logo.png)

#### A Collaborative Software Development Project
Date: February 9, 2018

Collaborators:

Bhatnagar, Tarini : [Github Profile](https://github.com/tarinib)

Guo, Xin (Alex): [Github Profile](https://github.com/alexguoxin)

Nikel, Indiana: [Github Profile](https://github.com/indiana-nikel)

#### Overview

According to a [study](http://comp.social.gatech.edu/papers/icwsm15.why.bakhshi.pdf) by Yahoo Labs, “Filtered photos are 21 percent more likely to be viewed and 45 percent more likely to be commented on. Have you ever wondered how you could tranform your images using filters similar to Instagram in Python?

We present this package that performs digital image processing.  It encompasses functions ranging from transformations like a simple flip, playing with color hues (rgb2gray) to 2D convolutions using a simple kernel matrix to do some interesting things! We have started with quite basic but diverse functions and hope to advance and add more with time.

#### Functions

###### Gaussian blur
This function performs convolution to de-emphasizes differences in adjacent pixel values. It has an averaging effect removing detail and noise resulting in blurring of the image.

>Input: image.jpg/png
>
>Output: blurred_image.jpg/png

###### Grayscale
This function converts an RGB image to grayscale. "amount" defines the proportion of conversion, with 100% leading to a complete grayscale and a value of 0% does not change the image at all.

>Input: image.jpg/png, amount
>
>Output: grayscale_image.jpg/png

###### Flip
This is a transformation function which flips the image either horizontally or vertically.

>Input: image.jpg/png, direction
>
>Output: flipped_image.jpg/png


#### Python ecosystem
"A picture paints a thousand words", however, a well-constructed image speaks even more than that without having to rely on a written description. We want to explore the elements of filters and their implementation in Python. A similar module called ["ImageFilter"](http://pillow.readthedocs.io/en/5.0.0/reference/ImageFilter.html) exists in Python which has standard filters like blur, sharpen, emboss among others.  We have started with a few basic functions but want to work towards building more advanced filters similar to the ones provided by Instagram.

#### Installation

To install InstaPy, follow these instructions:

1. Input the following into the Terminal: pip install git+https://github.com/UBC-MDS/InstaPy.git
2. You are good to go and can start using InstaPy!

#### Usage

```library(InstaPy)```

1.```flip(img_path,direction,output_path)```

Aruguments:

* ```img_path```: path to input image
* ```direction```: direction of flip. "h" (horizontal) or "v"(vertical)
* ```output_path```: path to output image
* Example: ```flip("./img.jpg", "h","./img_flip.jpg")```

2.```greyscale(img_path, output_path)```

Aruguments:

* ```img_path```: path to input image
* ```output_path```: path to output image
* Example: ```greyscale("./img.jpg", "./img_gs.jpg")```

3.```blur(img_path)```

Aruguments:

* ```img_path```: path to input image
* Example: ```blur("./img.jpg", "./img_blur.jpg")```



#### Package dependencies

```numpy```

```scipy.ndimage.filters```

```skimage.io```

```matplotlib.pyplot```

```sys```

```os```