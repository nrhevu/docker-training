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
CONTAINER ID   IMAGE                           COMMAND            CREATED          STATUS                      PORTS     NAMES
505fd6fa28fb   nrhevu/docker-training-s1:amd   "python test.py"   18 seconds ago   Exited (0) 17 seconds ago             exciting_blackwell
```

## Chạy một image
Chạy image `nrhevu/docker-training-s1` thành container sử dụng câu lệnh `docker run`

Kết quả hiển thị trên màn hình:
```
hello world!
```

## Dừng / Xóa một container
Dừng và xoá container đang chạy

Câu lệnh sử dụng:
```
docker stop bf8da7fe8499
docker rm bf8da7fe8499
```

## Chạy image với câu lệnh chỉ định
Chạy image `nrhevu/docker-training-s1` với câu lệnh `python test_custom.py`

Kết quả hiển thị trên màn hình:
```
#docker run --rm -it nrhevu/docker-training-s1:amd  python test_custom.py

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /
                    
```

## Hiển thị các container Docker đang chạy
Kết quả hiển thị trên màn hình:
```
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
docker run -d nrhevu/docker-training-s1:amd python test_api.py
```

## Xem logs của một container Docker đang chạy
Show log của container vừa chạy

Kết quả hiển thị trên màn hình:
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)
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
English: Hello
Vietnamese: Xin chào
French: Bonjour
Spanish: Hola
German: Hallo
Italian: Ciao
Portuguese: Olá
Russian: Здравствуйте (Zdravstvuyte)
Chinese (Mandarin): 你好 (Nǐ hǎo)
Japanese: こんにちは (Konnichiwa)
Korean: 안녕하세요 (Annyeonghaseyo)
Arabic: مرحبا (Marhaban)
Hindi: नमस्ते (Namaste)
Swedish: Hej
Dutch: Hallo
Greek: Γειά σας (Yia sas)
Turkish: Merhaba
Thai: สวัสดี (Sawasdee)
Hebrew: שלום (Shalom)
Zulu: Sawubonaroot
```

## Sao chép tệp từ/vào một container Docker
Lấy file `starter.txt` ra bên ngoài container

Nội dung của File: 
```
nglish: Hello
Vietnamese: Xin chào
French: Bonjour
Spanish: Hola
German: Hallo
Italian: Ciao
Portuguese: Olá
Russian: Здравствуйте (Zdravstvuyte)
Chinese (Mandarin): 你好 (Nǐ hǎo)
Japanese: こんにちは (Konnichiwa)
Korean: 안녕하세요 (Annyeonghaseyo)
Arabic: مرحبا (Marhaban)
Hindi: नमस्ते (Namaste)
Swedish: Hej
Dutch: Hallo
Greek: Γειά σας (Yia sas)
Turkish: Merhaba
Thai: สวัสดี (Sawasdee)
Hebrew: שלום (Shalom)
Zulu: Sawubonaroot
```