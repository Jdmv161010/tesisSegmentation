import cv2
import numpy as np

imagen = cv2.imread("grava.png")
imagen[np.all(imagen == 255, axis=2)]=0
#imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

kernel = np.array ([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype = np.float32)

imgLaplacian = cv2.filter2D (imagen, cv2.CV_32F, kernel)
agudo = np.float32 (imagen)
imgResult = agudo - imgLaplacian
# convertir de nuevo a escala de grises de 8 bits
imgResult = np.clip (imgResult, 0, 255)
imgResult = imgResult.astype ( 'uint8' )
imgLaplacian = np.clip (imgLaplacian, 0, 255)
imgLaplacian = np.uint8 (imgLaplacian)

bw = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
_, bw = cv2.threshold (bw, 40, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

dist = cv2.distanceTransform(bw, cv2.DIST_L2, 3)
cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)

_, dist = cv2.threshold(dist, 0.4, 1.0, cv2.THRESH_BINARY)
# Dilatar un poco la imagen dist
kernel1 = np.ones((3,3), dtype = np.uint8)
dist = cv2.dilate(dist, kernel1)

imagen = cv2.imwrite("grava1.png", dist)