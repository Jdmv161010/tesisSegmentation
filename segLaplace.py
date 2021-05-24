import numpy as np
import cv2

imagen = cv2.imread("grava.jpeg")
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(imagen, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imwrite("gravaLap.jpeg", lap)
