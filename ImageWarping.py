import cv2 
import numpy as np 

base_img = cv2.imread ("C:\\Users\\Asus\\OneDrive\\Documents\\CEVI\\images\\base_img.jpg")
subject = cv2.imread ("C:\\Users\\Asus\\OneDrive\\Documents\\CEVI\\images\\subject.jpg")

points = [[108, 186], [456 , 70] , [480 , 249] , [91 , 351]]

h_b , w_b , _ = base_img.shape
h_s, w_s , _= subject.shape

pts1 = np.float32([[0,0], [w_s,0] , [w_s, h_s], [0 , h_s]])
pts2 = np.float32(points)

trans_matrix = cv2.getPerspectiveTransform(pts1 , pts2)

print (trans_matrix)

warp_img = cv2.warpPerspective(subject , trans_matrix , (w_b , h_b))

mask  = np.ones(base_img.shape, dtype=np.uint8)*255
roi_corner = np.int32(points)

mask = cv2.fillConvexPoly(mask , roi_corner , (0,0,0))
mask_img = cv2.bitwise_and(mask , base_img)
mask_img = cv2.bitwise_or(mask_img , warp_img)
cv2.imshow("warp", mask_img)
cv2.waitKey(0)