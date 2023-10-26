import os
import subprocess

#đường dẫn đến công cụ opencv_createsample
createsamples_path=''
#đường dẫn đến công cụ TrainCascade
traincascade_path=''

#đường dẫn đến tập tin đối tượng
positive_sample_info='info.txt'
#Đường dẫn đến tập tin không chứa đối tượng
negative_sample_file='negative.txt'

#đường dẫn xuất file cascade.xml
output_dir='/out_put_dir'

#số lượng mẫu
num_positive_sample=1000
num_negative_sample=500

#kích thước ảnh mẫu
sample_width=24
sample_height=24

#tạo file vector từ tập huấn luyện và tập thông tin đối tượng
create_sample_command=[
    createsamples_path,
    "-info",positive_sample_info,
    "-vec",os.path.join(output_dir,"samples.vec"),
    "-w",str(sample_width),
    "-h",str(sample_height)
]
subprocess.call(create_sample_command)

#huấn luyện classifier từ file vec và tập không chứa đối tượng
train_cascade_command=[
    traincascade_path,
    "-data",output_dir,
    "-vec",os.path.join(output_dir,"samples.vec"),
    "-bg",negative_sample_file,
    "-numPos",str(num_positive_sample),
    "-numNeg",str(num_negative_sample),
    "-w",str(sample_width),
    "-h",str(sample_height)
]
subprocess.call(train_cascade_command)