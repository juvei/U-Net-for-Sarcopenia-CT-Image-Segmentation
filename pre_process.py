import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread('./input/input.png')

img1 = cv2.resize(img0.copy(),(1024,800))
for i in range(0,1024):
    for j in range(0,800):
        (img1[j,i,0],img1[j,i,1],img1[j,i,2])=(img0[j,i,0],img0[j,i,1],img0[j,i,2])

for i in range(0,1024):
    for j in range(0,800):
        if img1[j,i,1]>80 and img1[j,i,1]<200 and img1[j,i,2]>180:
            (img1[j,i,0],img1[j,i,1],img1[j,i,2])=(0,0,0)
        elif j<100 and i<50:
            (img1[j,i,0],img1[j,i,1],img1[j,i,2])=(0,0,0)

cv2.imwrite('./testing_set/input.png',img1)
cv2.imshow('resized',img1)

cv2.waitKey(0)
