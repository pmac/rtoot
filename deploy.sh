#!/bin/bash -ex

lektor plugins reinstall
lektor build -O public
cp _headers public/
