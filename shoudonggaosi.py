#导入基本库
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

def gaussian_filter(img,kernal_size,sigma):
    #先定义高斯卷积核
    kernal_size=int(kernal_size)
    center=kernal_size//2
    gaussian_kenral=np.zeros((kernal_size,kernal_size))
    for i in range(0,kernal_size):
        for j in range(0,kernal_size):
            gaussian_kenral[i][j]=1/(2*math.pi*sigma)*np.exp(-((-center+i)**2+(center-j)**2)/(2*sigma**2))
    gaussian_kenral=gaussian_kenral/gaussian_kenral.sum()#高斯核准备完成
    #进行高斯滤波，将卷积核与图像进行运算
    height=np.size(img,0)
    width=np.size(img,1)
    #进行高斯滤波后，得到的新图像尺寸大小
    new_height=height-kernal_size+1
    new_width=width-kernal_size+1
    new_image=np.zeros((new_height,new_width))
    #开始进行运算
    for i in range(0,new_height):
        for j in range(0,new_width):
            img_cell=img[i:i+kernal_size,j:j+kernal_size]
            new_image[i][j]=np.sum(gaussian_kenral*img_cell)
    return new_image

#读取图片，进行滤波
img = cv2.imread(r"/home/oem/下载/1021_1.jpg", cv2.IMREAD_GRAYSCALE)#cv2尽量全英文路径
kernal_size=30
sigma=50
img_blur=gaussian_filter(img,kernal_size,sigma)
#numpy矩阵直接用cv2容易出错，需将其转成8位
img_blur=np.array(img_blur,dtype=np.uint8)
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blurred Image', img_blur)
# 等待用户按键
cv2.waitKey(0)
cv2.destroyAllWindows()

#使用plt绘图
fig=plt.figure()
plt.subplots_adjust(top=1.19)
plt.subplot(2, 2, 1) # 第一张图片显示在第 1 个子图区域
plt.title("原图")
plt.imshow(img,cmap='gray')

plt.subplot(2, 2, 2) 
title="卷积核大小{},方差:{}".format(kernal_size,sigma)
plt.title(title)
plt.imshow(img_blur, cmap='gray')

plt.subplot(2, 2, 3) 
title="卷积核大小50,方差:100"
plt.title(title)
plt.imshow(gaussian_filter(img,50,100), cmap='gray')

plt.subplot(2, 2, 4) 
title="卷积核大小70,方差:120"
plt.title(title)
plt.imshow(gaussian_filter(img,70,120), cmap='gray')
plt.show()

