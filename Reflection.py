import cv2 
import numpy as np

img = cv2.imread("C:/Users/Asus/OneDrive/Documents/CEVI/images/BW.jpeg" , 0)

h,w = img.shape

new_img = np.zeros((h,w), dtype=np.uint8)

translation_Matrix = np.array(
    [[-1,0,0],
     [0,1,0],
     [0,0,1]] 
)

# rot_matrix = np.array(
#     [[0,1,0],
#      [1,0,0],
#      [0,0,1]] 
# )

for i in range (h):
    for j in range (w):
        co = np.array ([[i], [j] , [1]])
        new = np.dot(translation_Matrix, co)
        if new[0] > h-1 or new[1]>w-1:
            continue
        new_img[new[0] , new[1]] = img[i,j]

# for i in range (h):
#     for j in range (w):
#         co = np.array ([[i], [j] , [1]])
#         new = np.dot(rot_matrix, co)
#         if new[0] > h-1 or new[1]>w-1:
#             continue
#         new_img[new[0] , new[1]] = img[i,j]

cv2.imshow("Output", new_img)
cv2.waitKey(0)