import cv2
import math
import numpy as np
import tkinter as tk
from tkinter import messagebox

def show(title,message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title,message)
    root.destroy()

img0 = cv2.imread('./result/result.jpg')

# mask resize
img00 = cv2.resize(img0,(1024,1024),cv2.INTER_CUBIC)

mask = cv2.resize(img00.copy(),(1024,800))
for i in range(0,1024):
    for j in range(0,800):
        (mask[j,i,0],mask[j,i,1],mask[j,i,2])=(img00[j,i,0],img00[j,i,1],img00[j,i,2])

# mask
# 圖片size < 1024*800時會出問題
img1 = mask.copy()
input = cv2.imread('./testing_set/input.png')
for i in range(0,1024):
    for j in range(0,800):
        if mask[j,i,1]>50 and mask[j,i,2]>50:
            (img1[j,i,0],img1[j,i,1],img1[j,i,2])=(input[j,i,0],input[j,i,1],input[j,i,2])
        elif i>2 and i<100 and j>50 and j<750:
            (img1[j,i,0],img1[j,i,1],img1[j,i,2])=(input[j,i,0],input[j,i,1],input[j,i,2])
        else:
            (img1[j,i,0],img1[j,i,1],img1[j,i,2])=(0,0,0)

# 取出比例尺
bg = cv2.cvtColor(input.copy(),cv2.COLOR_BGR2GRAY)
img_empty = bg.copy()
img_empty[:,:] = 0
for i in range(0,1024):
    for j in range(0,800):
        if i>50 and i<974 and j>50 and j<750:
            bg[j,i] = 0
        elif j<50:
            bg[j,i] = 0
        elif i>974:
            bg[j,i] = 0
        elif j>750 and i<50:
            bg[j,i] = 0
        elif j>=799 or j<=1 or i>=1023 or i<=1:
            bg[j,i] = 0

contours,hierarachy = cv2.findContours(bg,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(bg,contours,-1,(255,255,255),2)

ruler15_xloc = 1023
ruler20_yloc = 0
for i in range(1023,-1,-1):
    if bg[399,i]>0:
        ruler15_xloc = i
for j in range(0,800):
    if bg[j,511]>0:
        ruler20_yloc = j

leng_ruler15 = 0
leng_ruler20 = 0
for i in range(0,1024):
    if bg[ruler20_yloc,i]>0:
        leng_ruler20 = leng_ruler20 + 1
    elif bg[ruler20_yloc,i-1]>0:
        break
for j in range(0,800):
    if bg[j,ruler15_xloc]>0:
        leng_ruler15 = leng_ruler15 + 1
    elif bg[j-1,ruler15_xloc]>0:
        break

print(ruler15_xloc,ruler20_yloc)
print(leng_ruler15,leng_ruler20)
# caluculate area
result_g = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
n=0
for i in range(0,1024):
    for j in range(0,800):
        if result_g[j,i]>=50:
            n = n+1
area = n*15*20/(leng_ruler15*leng_ruler20)#(315*420)
print('Area : ',area)

# Display
#cv2.imshow('origin',img00)
#cv2.imshow('input',input)
#cv2.imshow('resized mask',mask)
#cv2.imshow('filter',img1)
#cv2.imshow('bg',bg)
show("Area",f'Area : {area}')

cv2.waitKey(0)
