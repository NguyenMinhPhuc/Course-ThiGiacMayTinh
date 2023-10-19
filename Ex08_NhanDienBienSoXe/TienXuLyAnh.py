import cv2
import numpy as np

def preprocess_image(image):
    # Chuyển đổi ảnh sang không gian màu HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Cân bằng histogram kênh giá trị (Value) trong không gian màu HSV
    hsv_image[:,:,2] = cv2.equalizeHist(hsv_image[:,:,2])

    # Làm mờ ảnh để giảm nhiễu và làm rõ đặc trưng
    blurred_image = cv2.GaussianBlur(hsv_image, (5, 5), 0)

    # Áp dụng ngưỡng để tách biển số xe
    lower = np.array([0, 0, 0], dtype=np.uint8)
    upper = np.array([255, 255, 255], dtype=np.uint8)
    thresholded_image = cv2.inRange(blurred_image, lower, upper)

    return thresholded_image

def otsu_thresholding(image):
    # Chuyển đổi ảnh sang không gian màu grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng phương pháp Otsu's để xác định ngưỡng
    _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded_image

def adaptive_thresholding(image):
    # Chuyển đổi ảnh sang không gian màu grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng phương pháp Adaptive Thresholding để xác định ngưỡng
    thresholded_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    return thresholded_image
# Đường dẫn đến ảnh biển số xe
image_path = 'images.jpg'

# Đọc ảnh
image = cv2.imread(image_path)

# Tiền xử lý ảnh
preprocessed_image = preprocess_image(image)
preprocessed_image1 = otsu_thresholding(image)
preprocessed_image2 = adaptive_thresholding(image)
# Hiển thị ảnh gốc và ảnh đã tiền xử lý
cv2.imshow('Original Image', image)
cv2.imshow('Preprocessed Image', preprocessed_image)
cv2.imshow('preprocessed_image1', preprocessed_image1)
cv2.imshow('preprocessed_image2', preprocessed_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()