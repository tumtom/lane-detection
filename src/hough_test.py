import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy 
def nothing(x):
	pass

img = cv2.imread('road_640.jpg',0)
edges = cv2.Canny(img,212,414)

cv2.namedWindow('image')
cv2.createTrackbar('min','image',212,1000,nothing)
cv2.createTrackbar('max','image',414,1000,nothing)
cv2.createTrackbar('threshold','image',100,300,nothing)
cv2.createTrackbar('switch','image',0,2,nothing)
degree = 70
while(1):
	k = cv2.waitKey(100) & 0xFF
    	if k == 27:
        	break
	linelength = cv2.getTrackbarPos('linelength','image')
	gap = cv2.getTrackbarPos('gap','image')
	threshold = cv2.getTrackbarPos('threshold','image')
	mini = cv2.getTrackbarPos('min','image')
	maxi = cv2.getTrackbarPos('max','image')
	edges = cv2.Canny(img,mini,maxi)
	lines = cv2.HoughLines(edges,1,np.pi/180,threshold)
	img_lines = copy.copy(img)
	for rho,theta in lines[0]:
	    if (theta > 0 and theta < np.pi/180 * degree) or (theta > (np.pi/180 * (180-degree)) and theta < np.pi):
		    a = np.cos(theta)
		    b = np.sin(theta)
		    x0 = a*rho
		    y0 = b*rho
		    x1 = int(x0 + 1000*(-b))
		    y1 = int(y0 + 1000*(a))
		    x2 = int(x0 - 1000*(-b))
		    y2 = int(y0 - 1000*(a))
		    cv2.line(img_lines,(x1,y1),(x2,y2),(0,0,255),2)	
	if cv2.getTrackbarPos('switch','image') == 2: 
		cv2.imshow('image',img_lines)
	elif cv2.getTrackbarPos('switch','image') == 1:
		cv2.imshow('image',edges)
	else:
		cv2.imshow('image',img)


