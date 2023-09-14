#1. Thêm thư viên;
import cv2
#2. Đọc Video hoặc camera
#codec h264
video=cv2.VideoCapture(0)
#3. kiểm tra trạng thái video và xử lý

#Số lượng frame ảnh đã xử lý
frame_count=0

while video.isOpened():
    ret,frame=video.read()
    #kiểm tra trạng thái nếu ret==false thì thoát vòng lặp
    #ret=false khi hết video hoặc camera bị lỗi
    if not ret:
        break
    #thực hiện xử lý frame ảnh
    #Lưu từng frame ảnh thành file
    cv2.imwrite(f'Phan04_LamViecVoiVideo/BaiTapTrenLop/images/frame_{frame_count}.jpg',frame)

    #hiển thị ảnh lên cửa sổ
    cv2.imshow ("Video",frame)

    #cộng biến đếm frame_count
    frame_count+=1

    #Kiểm tra phím nhấn để tắt camera
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
# 4. giải phóng vùng nhớ cho chương trình
video.release()

#đóng cửa sổ hiển thị
cv2.destroyAllWindows()