# Phần 1
Chạy 1 vài câu lệnh cơ bản với Docker.

## Kéo 1 image từ Docker Hub
Kéo image `nrhevu/docker-training-s1` từ Docker Hub. Nếu sử dụng chip Intel, AMD thì kéo image `nrhevu/docker-training-s1:amd` về. Nếu sử dụng chip Apple Silicon hay Snapdragon thì kéo image `nrhevu/docker-training-s1:arm` về.

Câu lệnh sử dụng:
```
docker pull nrhevu/docker-training-s1:arm
```

## Hiển thị các image hiện có trong registry local
Kết quả hiển thị trên màn hình:
```
docker images
```

## Chạy một image
Chạy image `nrhevu/docker-training-s1` thành container sử dụng câu lệnh `docker run`

Kết quả hiển thị trên màn hình:
```
docker run nrhevu/docker-training-s1
```

## Dừng / Xóa một container
Dừng và xoá container đang chạy

Câu lệnh sử dụng:
```
docker stop [CONTAINER_ID]
docker rm [CONTAINER_ID]
```

## Chạy image với câu lệnh chỉ định
Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_custom.py`

Kết quả hiển thị trên màn hình:
```
docker run nrhevu/docker-training-s1 python test_custom.py
```

## Hiển thị các container Docker đang chạy
Kết quả hiển thị trên màn hình:
```
docker ps
```

## Chạy một image với câu lệnh volume
Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_volume.py` và tạo volume từ một thư mục đến ổ `/mount` khi chạy docker. Lúc này code sẽ tạo file `volume.txt` trong thư mục chỉ định

Kết quả hiển thị trên màn hình:
```
docker run -v /path/to/local/dir:/mount nrhevu/docker-training-s1 python test_volume.py
```
Nội dung trong file `volume.txt`:
```
Volume test successful!
```


## Chạy một image ở chế độ ngầm (background)
Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_api.py` ở chế độ ngầm.

Câu lệnh sử dụng:
```
docker run -d nrhevu/docker-training-s1 python test_api.py
```

## Xem logs của một container Docker đang chạy
Show log của container vừa chạy

Kết quả hiển thị trên màn hình:
```
docker logs [CONTAINER_ID]
```

## Mở cổng cho Docker
Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_api.py` và tạo thông kết nối đến cổng 8888 trong container. Sử dụng câu lệnh `curl localhost:8888` hoặc ứng dụng Postman để gọi API được cài trong Docker.


Kết quả hiển thị trên màn hình:
```
docker run -p 8888:8888 nrhevu/docker-training-s1 python test_api.py
```


## Truy cập vào một container đang chạy
Truy cập vào docker đang chạy và tìm file `starter.txt`, sử dụng lệnh `cat [FILE]` để xem nội dung.

Nội dung của File: 
```
docker exec -it [CONTAINER_ID] /bin/bash
```

## Sao chép tệp từ/vào một container Docker
Lấy file `starter.txt` ra bên ngoài container

Nội dung của File: 
```
cat starter.txt
```
