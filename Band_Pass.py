import numpy as np 
import cv2 as cv

img = cv.imread("C:\\Users\\Asus\\OneDrive\\Documents\\CEVI\\images\\animal.jpg" , 0)
t1 = 10
t2 = 200 

cv.imshow("img",img)
cv.waitKey(0)

h , w = (img.shape )

for i in range(h):
    for j in range(w):
        if (img[i][j] >t1 ) and (img[i][j] < t2) :
            img[i][j] = 0
        # else:
        #     img[i][j] = 255

        # print (img(i,j))

cv.imshow("img",img)
cv.waitKey(0)