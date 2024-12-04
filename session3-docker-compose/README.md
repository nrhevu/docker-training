# Phần 3
Dựng ứng dụng Elasticsearch và Kibana với docker-compose

Một đội phát triển dự án cần dựng ứng dụng Elasticsearch, Kibana. Đội dự án sử dụng các câu lệnh sau để dựng cụm:
```shell
docker network create es-net --driver=bridge

docker run -d \
--name es-container \
--net es-net \
-p 9200:9200 \
-e xpack.security.enabled=false \
-e discovery.type=single-node \
docker.elastic.co/elasticsearch/elasticsearch:7.11.0

docker run -d \
--name kb-container \
--net es-net \
-p 5601:5601 \
-e ELASTICSEARCH_HOSTS=http://es-container:9200 \
docker.elastic.co/kibana/kibana:7.11.0
```

Tuy nhiên mỗi lần muốn khởi động lại rất mất công. Vì vậy, hãy giúp đội dự án đơn giản hoá quy trình bằng cách sử dụng docker compose.