# Converting Image Format
# RGB to Grayscale

# rgb2gray module of skimage package is used to convert a 3-channel RGB Image to one channel monochrome image.
# In order to apply filters and other processing techniques,expected input is a 2D vector i.e. a monochrome image.
#
# skimage.color.rgb2gray() function : used to convert RGB image to Grayscale format

from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# setting the plot size to 15, 15
plt.figure(figsize=(15, 15))

# sample img of scikit-image package
coffee = data.coffee()
plt.subplot(1, 2, 1)

# displaying sample img
plt.imshow(coffee)

# converting rgb img to monochrome
gray_coffee = rgb2gray(coffee)
plt.subplot(1, 2, 2)

plt.imshow(gray_coffee, cmap="gray")
