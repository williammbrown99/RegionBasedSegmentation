#%%
#Imports
from skimage.color import rgb2gray

import numpy as np
import cv2
import matplotlib.pyplot as plt

from scipy import ndimage

# %%
#Reading and Printing Image
image = plt.imread('nature.jpg')
image.shape
plt.imshow(image)
plt.show()

# %%
#Convert Image to Grayscale
gray = rgb2gray(image)
plt.imshow(gray, cmap='gray')
plt.show()

# %%
#Check Shape of Image
print(gray.shape)

# %%
#Segmenting Image into 2 objects: Foreground and Background
#Reshaping Image to one dimentional array
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])

for i in range(gray_r.shape[0]):
        #If pixel value is greater than mean, pixel will be black
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 1 
    else:
        #If pixel value is less than or equal to mean, pixel will be white
        gray_r[i] = 0 

#Reshaping Image back to two dimensions
gray = gray_r.reshape(gray.shape[0],gray.shape[1])

#Showing new Image
plt.imshow(gray, cmap='gray')
plt.show()

# %%
#Segmenting Image into 4 Objects, Brighter closer to foreground
#Converting Image to grayscale
gray = rgb2gray(image)

#Coverting Image to 2 dimensions
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])

#Pixel value gets brighter as objects are closer to foreground
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 3
    elif gray_r[i] > 0.5:
        gray_r[i] = 2
    elif gray_r[i] > 0.25:
        gray_r[i] = 1
    else:
        gray_r[i] = 0

#Reshaping Image back to 2 dimensions
gray = gray_r.reshape(gray.shape[0],gray.shape[1])

#Printing Image
plt.imshow(gray, cmap='gray')
plt.show()

# %%
