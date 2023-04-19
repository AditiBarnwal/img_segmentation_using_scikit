# Importing Necessary Libraries
# Displaying the sample image - Monochrome Format
from skimage import data
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Sample Image of scikit-image package
coffee = data.coffee()
gray_coffee = rgb2gray(coffee)

# Setting the plot size to 15,15
plt.figure(figsize=(15, 15))

for i in range(10):
    # Iterating different thresholds
    binarized_gray = (gray_coffee > i * 0.1) * 1
    plt.subplot(5, 2, i + 1)

    # Rounding of the threshold
    # value to 1 decimal point
    plt.title("Threshold: >" + str(round(i * 0.1, 1)))

    # Displaying the binarized image
    # of various thresholds
    plt.imshow(binarized_gray, cmap='gray')

plt.tight_layout()

# Explanation: The first step in this thresholding is implemented by normalizing an image
# from 0 – 255 to 0 – 1. A threshold value is fixed and on the comparison, if evaluated to be true,
# then we store the result as 1, otherwise 0.
# This globally binarized image can be used to detect edges as well as analyze contrast and color difference.
