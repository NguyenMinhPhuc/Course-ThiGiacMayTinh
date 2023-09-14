import cv2

# Thiết lập thông số video
width = 640
height = 480
fps = 30
output_file = "Phan04_LamViecVoiVideo/output_video.mp4"

# Khởi tạo đối tượng VideoWriter với codec H.264
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Đọc video từ webcam
video = cv2.VideoCapture(0)

while True:
    # Đọc frame từ video
    ret, frame = video.read()

    # Kiểm tra nếu không đọc được frame, thoát khỏi vòng lặp
    if not ret:
        break

    # Thực hiện xử lý frame ở đây (nếu cần)

    # Ghi frame vào video
    out.write(frame)

    # Hiển thị frame
    cv2.imshow("Video", frame)

    # Kiểm tra phím nhấn để thoát (ấn 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng tệp video
video.release()
out.release()

# Đóng cửa sổ
cv2.destroyAllWindows()