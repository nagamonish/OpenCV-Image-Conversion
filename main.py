# Importing Open-CV module
import cv2 as img

# Reading the Image here
img1 = img.imread('sample.jpeg')

# COLOR_BGR2GRAY is the conversion code
# Takes in the original image and coverts its to gray
grayImg = img.cvtColor(img1, img.COLOR_BGR2GRAY)

# Converting the original image to an RGB converted image
rgbImg = img.cvtColor(img1, img.COLOR_BGR2RGB)

# Displays the original image
img.imshow('Original image', img1)

# Displays Image with gray background
img.imshow('Gray image', grayImg)

# Displays the RGB converted image
img.imshow('RGB image', rgbImg)

img.waitKey(0)
img.destroyAllWindows()

