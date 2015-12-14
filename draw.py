import cv2
import numpy as np
import math
import sys

def draw():
    im = cv2.imread('/Users/anthony/PycharmProjects/untitled/line-input.jpg')
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    real_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 1000): real_contours.append(contour)

    highY = highX = 0
    lowY = lowX = sys.maxint


    for point in real_contours[0]:
        if (point[0][0] > highX): highX = point[0][0]
        if (point[0][0] < lowX): lowX = point[0][0]
        if (point[0][1] > highY): highY = point[0][1]
        if (point[0][1] < lowY): lowY = point[0][1]


    def drawCorner(x, y):
        global img
        lowCalc = sys.maxint
        calc = 0
        for point in real_contours[0]:
            calc = abs((x - point[0][0])) + abs(y - point[0][1])
            if (lowCalc > calc):
                lowCalc = calc
                lowestPoint = point
        img = cv2.circle(im,(lowestPoint[0][0], lowestPoint[0][1]), 10, (0,0,255), -1)
        return lowestPoint


    point1 = drawCorner(highX, lowY)
    point2 = drawCorner(highX, highY)
    point3 = drawCorner(lowX, lowY)
    point4 = drawCorner(lowX, highY)

    def drawLine(pointA, pointB):
        cv2.line(im,(pointA[0][0], pointA[0][1]),(pointB[0][0], pointB[0][1]),(255,0,0),5)
        return math.hypot(pointA[0][0] - pointB[0][0], pointA[0][1] - pointB[0][1])


    distance_vert1 = drawLine(point1, point2);
    distance_vert2 = drawLine(point2, point3);
    distance_hor1 = drawLine(point3, point4);
    distance_hor2 = drawLine(point4, point1);

    distance_diag1 = drawLine(point1, point3);
    distance_diag2 = drawLine(point2, point4);

    #TODO calculate real distance



    cv2.imwrite('contours-output.jpg',im)
