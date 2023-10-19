import cv2
import pytesseract


def detect_license_plate(image_path):
    # Đọc ảnh đầu vào
    image = cv2.imread(image_path)

    # Chuyển đổi ảnh sang ảnh xám
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng bộ lọc Gauss để làm mờ ảnh
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Phát hiện các cạnh trong ảnh
    edged = cv2.Canny(blurred, 50, 150)

    # Tìm các đường viền trong ảnh
    contours, _ = cv2.findContours(
        edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # Sắp xếp các đường viền theo thứ tự từ trái qua phải
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    # Xác định đường viền biển số xe
    license_plate = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        # Điều kiện để xác định đường viền biển số xe
        if len(approx) == 4:
            license_plate = approx
            break

    if license_plate is None:
        print("Khong Tim Thay Bien So Xe")
        return None

    # Tạo khung bao quanh biển số xe
    cv2.drawContours(image, [license_plate], -1, (0, 255, 0), 2)

    # Cắt ảnh theo khung bao quanh biển số xe
    x, y, w, h = cv2.boundingRect(license_plate)
    plate_image = gray[y : y + h, x : x + w]

    # Sử dụng Tesseract để nhận diện văn bản
    custom_config = r"--oem 3 --psm 7"
    text = pytesseract.image_to_string(plate_image, config=custom_config)

    return text.strip(), image


# Đường dẫn tới ảnh đầu vào
image_path = "AnhXe.jpg"
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
# Nhận diện biển số xe và chuyển đổi thành văn bản
image_orign = cv2.imread(image_path, 1)
cv2.imshow("Orign", image_orign)
license_plate_text, image = detect_license_plate(image_path)
cv2.imshow("image", image)
print("Bien so Xe:", license_plate_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
