import numpy as np
import cv2
 
image = cv2.imread("grava.jpeg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(image,cv2.CV_64F,1,0) #x gradiente de dirección
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1) #y gradiente de dirección
 
sobelX = np.uint8(np.absolute(sobelX)) #x gradiente de dirección valor absoluto
sobelY = np.uint8(np.absolute(sobelY)) #y valor absoluto del gradiente de dirección
sobelCombined = cv2.bitwise_or(sobelX,sobelY)

canny = cv2.Canny(sobelCombined,30,150)

image[np.all(image == 255, axis=1)] = 10

#cv2.imwrite("SobelX.jpeg", sobelX)
#cv2.imwrite("SobelY.jpeg", sobelY)
#cv2.imwrite("SobelCombined.jpeg", sobelCombined)
cv2.imwrite("SobelCombinedCanny.jpeg", image)