#!/bin/bash -ex

lektor build -O _publish/build
cp Dockerfile nginx.conf _publish/
cd _publish
git init
git remote add dokku dokku@$DOKKU_HOST:$DOKKU_APP_NAME
git add .
git commit -m "add built site"
git push -f dokku master
