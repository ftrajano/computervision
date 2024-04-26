# In this script we are gonna load an image
# and learn how to use argparse :)

import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", 
				required = True,
				help = "path to input image")

ap.add_argument("-o", "--output", 
				required=True,
				help="path to output")


args = vars(ap.parse_args())

#image = cv2.imread('/Users/felipe/Public/computacao/computer-vision/images/ledzeppelin.png')
image = cv2.imread(args["image"])

# There is a little detail here.
# it would make more sense if the properties of the image
# were given as W x H 
# but in the way opencv works is more like a description 
# of a matrix, rows x columns 
# so height (that is the number of rows) versus width 
#( that's the number of columns)
(h, w , c) = image.shape

# display the image width, height, and number of color channels
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("color channels: {} pixels".format(c))

# show the image and wait for keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting
# image filetypes automatically)
cv2.imwrite("newImage.jpg", image)

# we can use the output argument as well to define 
# the name of the output
cv2.imwrite(args["output"]+".jpg", image)
