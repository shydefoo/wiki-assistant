#!/usr/bin/env bash

docker run --name wiki_db \
-e ALLOW_EMPTY_PASSWORD=yes \
-e MYSQL_DATABASE=wiki_database \
-p 3306:3306 \
-d \
bitnami/mysql