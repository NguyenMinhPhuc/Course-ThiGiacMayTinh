import cv2
import numpy as np
fx = 500.0
fy = 500.0
cx = 320.0
cy = 240.0

# Các thông số calibrate của camera
camera_matrix = np.array([[fx, 0, cx],
                          [0, fy, cy],
                          [0, 0, 1]])

k1 = 0.1
k2 = 0.2
p1 = 0.01
p2 = 0.02
k3 = 0.001
dist_coeffs = np.array([k1, k2, p1, p2, k3])
width = 10
height = 10
depth = 10
# Kích thước của vật thể (chiều rộng, chiều cao, chiều sâu)
object_size = (width, height, depth)

# Khởi tạo camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()

    if not ret:
        print("Không thể đọc frame từ camera.")
        break

    # Hiển thị frame
    cv2.imshow("Camera", frame)

    # Nhấn 'q' để thoát vòng lặp
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Chuyển đổi frame sang định dạng grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
x1 = 100
y1 = 200
x2 = 150
y2 = 250
x3 = 200
y3 = 300
x4 = 250
y4 = 350
# Tọa độ 2D của vật thể trên hình ảnh
object_points_2D = np.array([[x1, y1],[x2, y2],[x3, y3],[x4, y4]], dtype=np.float32)

# Tính toán tọa độ 3D của vật thể
success, rotation_vector, translation_vector = cv2.solvePnP(object_points_3D, object_points_2D, camera_matrix, dist_coeffs)

if success: # Tọa độ 3D
        object_point_3D = np.array([[0, 0, 0]], dtype=np.float32)
        object_point_3D, _ = cv2.projectPoints(
            object_point_3D, rotation_vector, translation_vector, camera_matrix, dist_coeffs
        )
        x_3D, y_3D, z_3D = object_point_3D[0][0]

        print("Tọa độ 3D của vật thể:")
        print(f"X: {x_3D} meters")
        print(f"Y: {y_3D} meters")
        print(f"Z: {z_3D} meters")
    else:
        print("Không thể tính toán tọa độ 3D của vật thể.")

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
