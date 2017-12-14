#!/usr/bin/env bash

docker-compose --file docker-compose.yml --file docker-compose-dev.yml build
docker-compose --file docker-compose.yml --file docker-compose-dev.yml down
docker-compose --file docker-compose.yml --file docker-compose-dev.yml up
