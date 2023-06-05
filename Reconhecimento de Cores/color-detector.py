# import os imports the os module, which provides functions for interacting with the operating system.
# 
# import cv2 imports the OpenCV library, which is used for computer vision tasks.
# 
# cj = 'cj.jpg' assigns the string 'cj.jpg' to the variable cj. This variable represents the filename or relative path of the image file.
# 
# os.path.join('.', cj) joins the current directory ('.') and the filename (cj) to create the complete path to the image file. This is done using the os.path.join function.
# 
# cv2.imread(os.path.join('.', cj)) reads the image file specified by the path obtained in the previous step using os.path.join. The cv2.imread function reads the image and # returns a NumPy array representation of the image. This array is assigned to the variable img.
# 
# cv2.cvtColor(img, cv2.COLOR_BGR2RGB) converts the color space of the img array from BGR (Blue-Green-Red) to RGB (Red-Green-Blue). The cv2.cvtColor function is used for # color space conversions. The resulting RGB image is assigned to the variable img_rgb.
# 
# cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) converts the color space of the img array from BGR to grayscale. The resulting grayscale image is assigned to the variable img_gray.
# 
# cv2.imshow('img', img), cv2.imshow('img_rgb', img_rgb), and cv2.imshow('img_gray', img_gray) display the images in separate windows. The first argument is the window # name, and the second argument is the image array to be displayed.
# 
# cv2.waitKey(0) waits until a key is pressed to close the windows. The argument 0 means it waits indefinitely until a key event occurs.
# 
# In summary, this code reads an image file, converts it to RGB and grayscale color spaces, and displays the original, RGB, and grayscale images in separate windows. The code uses the os module to handle paths, the cv2 library for image operations, and the NumPy library for array manipulation.

import os
import cv2

gallery = './gallery'



def generateAll():
  for image in gallery:
    img = cv2.imread(os.path.join('.', image))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_edge = cv2.Canny(img, 10, 50)
    cv2.imshow('img', img)
    cv2.imshow('img_rgb', img_rgb)
    cv2.imshow('img_gray', img_gray)
    cv2.imshow('img_edge', img_edge)
    
generateAll()
cv2.waitKey(0)