#!/bin/bash

# Network
docker network create net-aula5

# Container do app node
docker build -t app .
docker run -d --network net-aula5 --name app app

# Container do caso de teste
docker build -f ./Dockerfile_test -t teste-aula5 .
docker run --network net-aula5 teste-aula5