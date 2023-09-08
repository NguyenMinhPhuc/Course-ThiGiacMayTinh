import cv2
import numpy as np
from skimage.feature import hog

# Đọc ảnh
image = cv2.imread('Phan3_CacThuatToantienXuLyAnh/ApDungTimContour/sample.png')

# Chuyển đổi ảnh sang ảnh xám
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Áp dụng Gaussian Blur để làm mờ ảnh
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Áp dụng phân ngưỡng để tạo ảnh nhị phân
_, thresholded = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

# Tìm các contour trong ảnh nhị phân
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ các contour lên ảnh gốc
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Trích xuất đặc trưng HOG từ ảnh xám
features, _ = hog(gray, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)

# In kích thước của vector đặc trưng HOG
print("Kich thuoc vector dac trung HOG:", features.shape)

# Hiển thị ảnh gốc và ảnh nhị phân
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()