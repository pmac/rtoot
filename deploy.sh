#!/bin/bash -ex

git branch -D build
git checkout -b build
lektor build -O build
git add build
git commit -m "add built site"
git push -f dokku build:master
git checkout -
