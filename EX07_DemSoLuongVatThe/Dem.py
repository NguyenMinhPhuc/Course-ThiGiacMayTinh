import cv2
import numpy as np

def preprocess_image(image):
    # Chuyển đổi sang ảnh grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Làm mờ ảnh bằng bộ lọc Gaussian
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Phân ngưỡng ảnh để tạo ảnh nhị phân
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Xử lý biên bằng phương pháp Canny
    edges = cv2.Canny(thresh, 30, 150)

    return edges

def count_iron_rings(image):
    # Tiền xử lý ảnh
    edges = preprocess_image(image)

    # Tìm các đường contour trong ảnh
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Đếm số lượng vòng sắt
    iron_ring_count = 0
    for contour in contours:
        # Lọc contour dựa trên diện tích
        area = cv2.contourArea(contour)
        if area > 100:  # Điều chỉnh ngưỡng diện tích tùy theo ảnh cụ thể
            iron_ring_count += 1

    return iron_ring_count

# Đọc ảnh
image = cv2.imread('images/download.jpg')

# Đếm số lượng vòng sắt
count = count_iron_rings(image)
print("SL: ", count)