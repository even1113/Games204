import cv2

# Image acquisition
image = cv2.imread("input_image.jpg")

# Pre-processing
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Feature extraction
edges = cv2.Canny(gray_image, 100, 200)

# Decision making
(contours, _) = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Output
output_image = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imwrite("output_image.jpg", output_image)
