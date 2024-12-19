FROM nrhevu/docker-training-s1:amd

COPY test_copy_file.txt /root

WORKDIR /root

RUN apt-get update && apt-get install -y tree

ENV YOU="nguyenluonguy"

EXPOSE 8888

CMD ["python", "/app/test_api.py"]