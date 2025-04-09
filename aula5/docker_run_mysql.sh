#!/bin/bash

docker run --name mysql_container \
 --network minha-rede \
 -e MYSQL_ROOT_PASSWORD=123 \
 -e MYSQL_DATABASE=meu_db \
 -p 3306:3306 \
 -d \
 mysql:8.0
