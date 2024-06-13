import cv2 as cv
import numpy as np 
img1 = cv.imread("C:\\Users\\Asus\\OneDrive\\Documents\\CEVI\\images\\animal.jpg",0)
img2 = cv.imread("C:\\Users\\Asus\\OneDrive\\Documents\\CEVI\\images\\Lenna.png",0)

alpha  = float (input ("Enter alpha "))
beta = float(input ("Enter beta "))
gamma = float (input ("Enter gamma "))
#alpha = beta = gamma = 0.5
img2=cv.resize(img2, (500,500))
img1=cv.resize(img1, (500,500))

cv.imshow("Img" , img1)
cv.waitKey(0)

h , w = img1.shape

img = np.zeros((h,w) , dtype=int)

print (img1.shape)

for i in range (h):
    for j in range (w):
         img[i][j] = alpha * img1[i][j] + beta* img2[i][j] + gamma

img = np.uint8(img)

cv.imshow("Img" , img)
cv.waitKey(0)
