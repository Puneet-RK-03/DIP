import cv2 
import numpy as np

img = cv2.imread("C:/Users/Asus/OneDrive/Documents/CEVI/images/BW.jpeg" , 0)

h,w = img.shape
theta = 45 
new_img = np.zeros((2*h,2*w), dtype=np.uint8)
print(np.cos(np.pi / 4))
Matrix = np.array(
    [[np.cos(np.pi / 4), -np.sin(np.pi / 4) ,0],
     [np.sin(np.pi / 4),np.cos(np.pi / 4) ,0],
     [0,0,1]] 
)


for i in range (h):
    for j in range (w):
        co = np.array ([[i], [j] , [1]])
        new = np.dot(Matrix, co)
        if new[0] > h-1 or new[1]>w-1:
            continue
        new_img[int(new[0]) , int(new[1])] = img[i,j]

# for i in range (h):
#     for j in range (w):
#         co = np.array ([[i], [j] , [1]])
#         new = np.dot(rot_matrix, co)
#         if new[0] > h-1 or new[1]>w-1:
#             continue
#         new_img[new[0] , new[1]] = img[i,j]

cv2.imshow("Output", new_img)
cv2.waitKey(0)