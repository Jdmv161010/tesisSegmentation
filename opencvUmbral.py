import cv2
import numpy as np

imagen = cv2.imread("grava.png")
imgGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

umbral, imagenMetodo = cv2.threshold(imgGris, 0, 255, cv2.THRESH_OTSU)
mascara = np.uint8((imgGris<umbral)*255)

cv2.imwrite("mascara.jpg", mascara)
cv2.imwrite("imagenMetodo.jpg", imagenMetodo)

numlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(mascara, 4, cv2.CV_32S)

print(numlabels)