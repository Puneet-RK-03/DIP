import numpy as np
import cv2

def harris_corner_detection(image, k=0.04, threshold=0.01):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    # Compute derivatives in x and y direction using Sobel operator
    Ix = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    Iy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

    # Compute the elements of the structure tensor
    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy

    # Apply Gaussian smoothing to the elements of the structure tensor
    kernel_size = 5
    sigma = 1.5
    Ixx = cv2.GaussianBlur(Ixx, (kernel_size, kernel_size), sigma)
    Iyy = cv2.GaussianBlur(Iyy, (kernel_size, kernel_size), sigma)
    Ixy = cv2.GaussianBlur(Ixy, (kernel_size, kernel_size), sigma)

    # Compute the Harris response
    det_M = Ixx * Iyy - Ixy * Ixy
    trace_M = Ixx + Iyy
    response = det_M - k * (trace_M ** 2)

    # Threshold the response to identify corner points
    corners = np.argwhere(response > threshold * response.max())

    return corners

# Load the image
image = cv2.imread('C:\\Users\\Asus\\OneDrive\\Documents\\CEVI\\images\\square.png')

# Perform Harris Corner Detection
corners = harris_corner_detection(image)

# Draw circles around the detected corners
for corner in corners:
    x, y = corner[1], corner[0]
    cv2.circle(image, (x, y), 5, (0, 0, 255), -1)  # Red circle

# Display the image with detected corners
cv2.imshow('Harris Corner Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
