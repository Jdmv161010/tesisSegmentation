
import numpy as np
import cv2
 
image = cv2.imread("grava.jpeg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
canny = cv2.Canny(image,30,150)
cv2.imwrite("Canny.jpeg",canny)
