#1. Thêm thư viên;
import cv2
#2. Đọc Video hoặc camera
#codec h264
video=cv2.VideoCapture(0)


#3. Khai báo thông số của Video cần lưu
width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps= 30 #số khung hình mỗi giây
out_file='Phan04_LamViecVoiVideo/BaiTapTrenLop/videos/Video_Output_Gray.mp4'
#3.1. Khởi tạo đối tượng video Writer
fourcc=cv2.VideoWriter_fourcc(*"mp4v")#codec H264
out=cv2.VideoWriter(out_file,fourcc,fps,(width,height),isColor=True)

#4. kiểm tra trạng thái video và xử lý
while video.isOpened():
    ret,frame=video.read()
    #kiểm tra trạng thái nếu ret==false thì thoát vòng lặp
    #ret=false khi hết video hoặc camera bị lỗi
    if not ret:
        break
    #Chuyen Anh xam
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #thực hiện ghi frame ảnh vào video out
    out.write(gray_frame)

    #hiển thị ảnh lên cửa sổ
    cv2.imshow ("Video",frame)
    cv2.imshow ("Gray",gray_frame)

    #Kiểm tra phím nhấn để tắt camera
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
# 4. giải phóng vùng nhớ cho chương trình
video.release()
out.release()
#đóng cửa sổ hiển thị
cv2.destroyAllWindows()



