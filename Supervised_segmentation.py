# Supervised Segmentation
# For this segmentation, it requires external input.
# This includes things like setting a threshold, converting formats, and correcting external biases.
#
# @Segmentation by Thresholding – Manual Input
# An external pixel value ranging from 0 to 255 is used to separate the picture from the background.
# This results in a modified picture that is larger or less than the specified threshold.


# @Segmentation by Thresholding  Using skimage.filters module
#  - Niblack and Sauvola thresholding technique : to improve the quality of microscopic images.
#    It’s a local thresholding approach that changes the threshold depending
#    on the local mean and standard deviation for each pixel in a sliding window.
#    Otsu’s thresholding technique works by iterating over all possible threshold values and
#    computing a measure of dispersion for the sample points on either side of the threshold,
#    i.e. either in foreground or background.

# {{ 1.
# skimage.filters.threshold_otsu() function is used to return threshold value based on Otsu’s method.
# Syntax : skimage.filters.threshold_otsu(image)
# Parameters :
# image : An image – Monochrome format
# nbins : Number of bins required for histogram calculation
# hist : Histogram from which threshold has to be calculated
# Return : threshold : Larger pixel intensity
# }}


# {{ 2.
# skimage.filters.threshold_niblack() function is a local thresholding function that
# returns a threshold value for every pixel based on Niblack’s method.
#
# Syntax : skimage.filters.threshold_niblack(image)
# Parameters :
# image : An image – Monochrome format
# window_size : Window size – odd integer
# k : A positive parameter

# Return : threshold : A threshold mask equal to the shape of the image
# }}


# {{ 3.
# skimage.filters.threshold_sauvola() function is a local thresholding function that
# returns a threshold value for every pixel based on Sauvola’s method.
#
#
# Syntax : skimage.filters.threshold_sauvola(image)
#
# Parameters :
#
# image : An image – Monochrome format
# window_size : Window size – odd integer
# k : A positive parameter
# r : A positive parameter – dynamic range of standard deviation
# Return - threshold : A threshold mask equal to the shape of the image
# }}


# @Active Contour Segmentation
# The concept of energy functional reduction underpins the active contour method.
# An active contour is a segmentation approach that uses energy forces and restrictions
# to separate the pixels of interest from the remainder of the picture for further processing and analysis.
# “active contour” : a model in the segmentation process.
#
# skimage.segmentation.active_contour() function active contours by fitting snakes to image features
# Syntax : skimage.segmentation.active_contour(image, snake)
# Parameters :
# image : An image
# snake : Initial snake coordinates – for bounding the feature
# alpha : Snake length shape
# beta : Snake smoothness shape
# w_line : Controls attraction – Brightness
# w_edge : Controls attraction – Edges
# gamma : Explicit time step
# Return - snake : Optimised snake with input parameter’s size


# @Chan-Vese Segmentation

# skimage.segmentation.chan_vese() function is used to segment objects using the
# Chan-Vese Algorithm whose boundaries are not clearly defined.
#
# Syntax : skimage.segmentation.chan_vese(image)
# Parameters :
# image : An image
# mu : Weight – Edge Length
# lambda1 : Weight – Difference from average
# tol : Tolerance of Level set variation
# max_num_iter : Maximum number of iterations
# extended_output : Tuple of 3 values is returned
# Return : segmentation : Segmented Image
#          phi : Final level set
#          energies: Shows the evolution of the energy
