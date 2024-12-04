FROM nrhevu/docker-training-s1:arm

COPY test_copy_file.txt /root/

WORKDIR /root

# EXPOSE 8888

RUN apt-get update && apt-get install tree

ENV YOU="nguyenthevu"

CMD [ "python" , "/app/test_api.py"]