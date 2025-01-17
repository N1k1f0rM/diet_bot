#!/bin/bash

cd ~

rm -rf ./diet_bot

git clone https://github.com/N1k1f0rM/diet_bot.git

cd diet_bot

docker stop diet_container
docker rm diet_container
docker rmi diet_bot
docker build -t diet_bot .
docker run --name diet_container --env-file=../.env -d diet_bot
