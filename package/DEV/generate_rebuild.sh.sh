#!/bin/bash


#define parameters which are passed in.
NAME=$1
PORT=$2
SSH=$3

#define the template.
cat  << EOF
docker stop $NAME
docker rm $NAME
(cd main/ && docker build -t $NAME .)
docker run -d --name $NAME -p 127.0.0.1:$PORT:80 $NAME
EOF