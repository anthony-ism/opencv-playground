import cv2
import numpy as np
from matplotlib import pyplot as plt


#im = cv2.imread('/Users/anthony/opencv/orignal.jpg')
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
img = cv2.imread('/Users/anthony/opencv/black-to-white-input.jpg', 0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
lines = cv2.HoughLinesP(edges, 1, 3.14/180, 70, 30, 10);

plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

