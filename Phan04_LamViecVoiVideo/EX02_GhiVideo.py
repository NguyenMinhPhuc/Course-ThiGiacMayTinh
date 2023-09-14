import cv2

# Đọc video từ webcam
video = cv2.VideoCapture(0)

# Thiết lập thông số video
width = 640
height = 480
fps = 30  # số khung hình mỗi giây
output_file = "Phan04_LamViecVoiVideo/output_video1.mp4"

# Tạo đối tượng VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height),isColor=False)

while True:
    # Đọc frame từ video
    ret, frame = video.read()

    # Kiểm tra nếu không đọc được frame, thoát khỏi vòng lặp
    if not ret:
        break

    # Áp dụng hiệu ứng xám (grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ghi frame vào video
    out.write(gray_frame)

    # Hiển thị frame gốc và frame đã xử lý
    cv2.imshow("Original", frame)
    cv2.imshow("Grayscale", gray_frame)

    # Kiểm tra phím nhấn để thoát (ấn 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng tệp video
video.release()
out.release()

# Đóng cửa sổ
cv2.destroyAllWindows()