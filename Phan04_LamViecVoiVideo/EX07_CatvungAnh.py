import cv2

# Mở video để đọc
video_capture = cv2.VideoCapture(0)

# Xác định vùng ảnh cần cắt (điểm trái trên và điểm phải dưới)
top_left = (100, 100)        # (x, y) của điểm trái trên
bottom_right = (300, 300)    # (x, y) của điểm phải dưới

# Tạo đối tượng VideoWriter để lưu video cắt
output_video = cv2.VideoWriter("Phan04_LamViecVoiVideo/output_videovung.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30.0, (bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]))

# Đọc và lưu các khung hình
while True:
    # Đọc khung hình
    ret, frame = video_capture.read()

    # Kiểm tra xem việc đọc khung hình thành công hay không
    if not ret:
        break

    # Cắt vùng ảnh cần lưu
    cropped_frame = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

    # Lưu khung hình đã cắt vào video đầu ra
    output_video.write(cropped_frame)

    # Hiển thị frame gốc và frame đã xử lý
    cv2.imshow("Original", frame)

    # Kiểm tra phím nhấn để thoát (ấn 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
video_capture.release()
output_video.release()

# Đóng cửa sổ
cv2.destroyAllWindows()