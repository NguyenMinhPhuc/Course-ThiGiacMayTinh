#thực 2 mục tiêu
#1. cấu trúc cho chương trình nhận diện sản phẩm
#2. Xây dựng tạo file đặc trưng *.xml

import cv2
import time
import datetime

# Khởi tạo bộ đếm và biến đếm
counter = 0

cap = cv2.VideoCapture(0)  # Số 0 để chọn camera mặc định

# Định nghĩa hàm đếm sản phẩm
def count_objects(image,cascade_path):
    # tiền xử lý ảnh
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Tạo bộ phát hiện đối tượng
    cascade=cv2.CascadeClassifier(cascade_path)
    #phát hiện tối tượng
    objects=cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    count=len(objects)

    return count  # Thay bằng kết quả thực tế

cascade_path='haarcascade_frontalface_default.xml'

#đọc tỉ lệ khung hình
frame_rate=cap.get(cv2.CAP_PROP_FPS)

#tính thời gian trở giữa mỗi frame
second_number=1
wait_time=int(second_number*1000/frame_rate)
# Khởi tạo video capture từ camera
#biến dếm thời gian
start_time=time.time()
elapsed_time=0
while True:
    # Đọc frame từ video capture
    ret, frame = cap.read()

    if not ret:
        break
    #KIỂM TRA ĐỦ GIÂY CHƯA
    current_time=time.time()
    elapsed_time+=current_time-start_time
    start_time=current_time

    if elapsed_time>=second_number:
    # Thực hiện xử lý ảnh để đếm số lượng sản phẩm
        count = count_objects(frame,cascade_path)
        counter+=count

        elapsed_time=0

    # Hiển thị số lượng sản phẩm trên frame
    cv2.putText(frame, "Count: {}".format(counter), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(frame, "Time: {}".format(elapsed_time), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    #current time
    current_time_Display=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, "Current time: {}".format(current_time_Display), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # Hiển thị frame
    cv2.imshow("Counting Objects", frame)
    # Kiểm tra phím nhấn 'q' để thoát
    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()