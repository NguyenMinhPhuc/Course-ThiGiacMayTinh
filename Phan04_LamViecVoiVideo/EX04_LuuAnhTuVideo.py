import cv2

# Mở video để đọc
video_capture = cv2.VideoCapture(0)

# Đọc và lưu các khung hình
frame_count = 0
while True:
    # Đọc khung hình
    ret, frame = video_capture.read()

    # Kiểm tra xem việc đọc khung hình thành công hay không
    if not ret:
        break

    # Lưu khung hình thành file ảnh
    cv2.imwrite(f"Phan04_LamViecVoiVideo/Images/frame_{frame_count}.jpg", frame)
    cv2.imshow("Original", frame)
    # Tăng số lượng khung hình đã lưu
    frame_count += 1
    # Kiểm tra phím nhấn để thoát (ấn 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
video_capture.release()
# Đóng cửa sổ
cv2.destroyAllWindows()