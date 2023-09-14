import cv2

# Đọc video từ webcam
video = cv2.VideoCapture('Phan04_LamViecVoiVideo/sample.avi')

while True:
    # Đọc frame từ video
    ret, frame = video.read()

    # Kiểm tra nếu không đọc được frame, thoát khỏi vòng lặp
    if not ret:
        break

    # Hiển thị frame
    cv2.imshow("Video", frame)

    # Kiểm tra phím nhấn để thoát (ấn 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng cửa sổ
video.release()
cv2.destroyAllWindows()