# Phần 1

Chạy 1 vài câu lệnh cơ bản với Docker.

## Kéo 1 image từ Docker Hub

Kéo image `nrhevu/docker-training-s1` từ Docker Hub. Nếu sử dụng chip Intel, AMD thì kéo image `nrhevu/docker-training-s1:amd` về. Nếu sử dụng chip Apple Silicon hay Snapdragon thì kéo image `nrhevu/docker-training-s1:arm` về.

Câu lệnh sử dụng:

```
docker pull nrhevu/docker-training-s1:amd
```

## Hiển thị các image hiện có trong registry local

Kết quả hiển thị trên màn hình:

```
> docker image ls

REPOSITORY                   TAG             IMAGE ID       CREATED        SIZE
nrhevu/docker-training-s1    amd             f413332958a8   9 hours ago    803MB
nghiaphunng18/mukapet-demo   0.0.2           d8c9bc2f20ba   3 weeks ago    561MB
mukapet-demo                 0.0.2           d8c9bc2f20ba   3 weeks ago    561MB
<none>                       <none>          492c77406142   3 weeks ago    561MB
mysql                        8.0.36-debian   81112135876a   8 months ago   601MB
```

## Chạy một image

Chạy image `nrhevu/docker-training-s1` thành container sử dụng câu lệnh `docker run`

Kết quả hiển thị trên màn hình:

```
> docker run nrhevu/docker-training-s1:amd
hello world!
```

## Dừng / Xóa một container

Dừng và xoá container đang chạy

Câu lệnh sử dụng:

```
docker ps
docker rm quirky_chatelet
docker stop quirky_chatelet
```

## Chạy image với câu lệnh chỉ định

Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_custom.py`

Kết quả hiển thị trên màn hình:

```
docker run -d nrhevu/docker-training-s1:amd python test_custom.py
 > 79c65dde39ed5e3c65117a1336166398939f4ab117e12bed51b9c7fa18944ff5
```

## Hiển thị các container Docker đang chạy

Kết quả hiển thị trên màn hình:

```
 > docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Chạy một image với câu lệnh volume

Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_volume.py` và tạo volume từ một thư mục đến ổ `/mount` khi chạy docker. Lúc này code sẽ tạo file `volume.txt` trong thư mục chỉ định

Kết quả hiển thị trên màn hình:

```
...
```

Nội dung trong file `volume.txt`:

```
...
```

## Chạy một image ở chế độ ngầm (background)

Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_api.py` ở chế độ ngầm.

Câu lệnh sử dụng:

```
docker run -d nrhevu/docker-training-s1:amd python test_custom.py
```

## Xem logs của một container Docker đang chạy

Show log của container vừa chạy

Kết quả hiển thị trên màn hình:

```
...
```

## Mở cổng cho Docker

Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_api.py` và tạo thông kết nối đến cổng 8888 trong container. Sử dụng câu lệnh `curl localhost:8888` hoặc ứng dụng Postman để gọi API được cài trong Docker.

Kết quả hiển thị trên màn hình:

```
...
```

## Truy cập vào một container đang chạy

Truy cập vào docker đang chạy và tìm file `starter.txt`, sử dụng lệnh `cat [FILE]` để xem nội dung.

Nội dung của File:

```
...
```

## Sao chép tệp từ/vào một container Docker

Lấy file `starter.txt` ra bên ngoài container

Nội dung của File:

```
...
```
