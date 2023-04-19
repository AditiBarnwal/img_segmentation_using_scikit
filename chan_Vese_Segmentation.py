# Chan-Vese iterative segmentation method splits a picture into two groups with the lowest intra-class variance.
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.segmentation import chan_vese

fig, axes = plt.subplots(1, 3, figsize=(10, 10))

# Sample Image of scikit-image package
coffee = data.coffee()
gray_coffee = rgb2gray(coffee)

# Computing the Chan VESE segmentation technique
chanvese_gray_coffee = chan_vese(gray_coffee , extended_output=True)

ax = axes.flatten()

# Plotting the original image
ax[0].imshow(gray_coffee, cmap="gray")
ax[0].set_title("Original Image")

# Plotting the segmented - 100 iterations image
ax[1].imshow(chanvese_gray_coffee[0], cmap="gray")
title = "Chan-Vese segmentation - {} iterations".format(len(chanvese_gray_coffee[2]))

ax[1].set_title(title)

# Plotting the final level set
ax[2].imshow(chanvese_gray_coffee[1], cmap="gray")
ax[2].set_title("Final Level Set")
plt.show()


# read abt this not sure
# it worked.....yeahhhhh
