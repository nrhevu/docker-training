# Phần 2
Viết Dockerfile để build một image có thể thoả mãn các testcases sau:

## Test 1: Image được build từ image gốc lên
Build một image mới từ một image có sẵn, sử dụng image `nrhevu/docker-training-s1:[TAG]`. 

Chạy câu lệnh `docker run [IMAGE_ID] cat /app/starter.txt`. Nếu màn hình hiện ra câu chào từ các thứ tiếng là Đạt.

## Test 2: Đặt tên cho image mới build 
Đặt tên image là `nrhevu/docker-training-s2`, tag là tên của bạn viết tắt cùng với mã số sinh viên, ví dụ tên là `Nguyễn Thế Vũ` thì đặt là `vunt241147m`. 

Sau khi build thành công, chạy câu lệnh `docker images` để kiểm tra image vừa tạo. Nếu trong list images có image với tên vừa tạo là Đạt.

## Test 3: Copy 1 file bên ngoài vào trong Docker image
Copy file `test_copy_file.txt` vào thư mục `/root` trong image.

Chạy câu lệnh `docker run nrhevu/docker-training-s2:vunt241147m cat /root/test_copy_file.txt` để kiểm tra. Nếu màn hình hiện ra nội dung file là Đạt.

## Test 4: Thay đổi đường dẫn mặc định
Thay đổi đường dẫn mặc định của docker image thành `/root`.

Chạy câu lệnh `docker run nrhevu/docker-training-s2:vunt241147m pwd`, nếu màn hình hiện ra `/root` là Đạt

## Test 5: Chạy lệnh trong quá trình build Docker Image
Cài đặt gói `tree` của linux, sử dụng câu lệnh `apt-get install` để cài đặt.

Chạy câu lệnh `docker run nrhevu/docker-training-s2:vunt241147m tree / -L 1`, nếu màn hình hiện ra cây thư mục là thành công.

## Test 6: Đặt biến môi trường 
Cài đặt biến môi trường trong docker image `YOU` thành tên của bạn.

Chạy câu lệnh `docker run nrhevu/docker-training-s2:vunt241147m python -c 'import os;print(os.environ["YOU"])'`, nếu màn hình hiện ra giá trị biến là Đạt.

## Test 7: Đặt lệnh mặc định khi chạy Docker Image
Đặt câu lệnh mặc định khi chạy docker image là `python /app/test-api.py`.

Chạy lệnh `docker run nrhevu/docker-training-s2:vunt241147m`, nếu màn hình hiện ra log chạy là Đạt.

## Test 8: Mở Port khi build Docker Image
Mở port 8888 khi build docker image.
Chạy lệnh `docker run -d -P nrhevu/docker-training-s2:vunt241147m` để chạy docker, flag `-P` là để tạo port kết nối thông với bên ngoài với những port kết nối đã chỉ định. Chạy lệnh `docker ps` để kiểm tra port mà docker cho phép. Chạy lệnh `curl localhost:[PORT]` để kiểm tra. Nếu lệnh chạy thành công là Đạt.