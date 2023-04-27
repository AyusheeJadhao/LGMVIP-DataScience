"""This module provides functions to perform image processing tasks using OpenCV."""
import cv2

# Rest of the code
# Reading image data
sketch = cv2.imread("Flower23.png")

# Converting image in grey scale
grey_scale = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output1.png", grey_scale)

# Converting grey scale image into inverted image
invert_sketch = cv2.bitwise_not(grey_scale)
cv2.imwrite("output2.png", invert_sketch)

# Converting inverted image into blur image
blur_sketch = cv2.GaussianBlur(invert_sketch, (21,21),0)
cv2.imwrite("output3.png", blur_sketch)

# Converting blur image into blur image by fliping pixel values
invertedblur = cv2.bitwise_not(blur_sketch)
cv2.imwrite("output4.png", invertedblur)

# finale output
sketch_filter = cv2.divide(grey_scale,invertedblur,scale=250.0)
cv2.imwrite("floweroutput.png", sketch_filter)