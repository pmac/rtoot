#!/bin/bash -ex

lektor build -O public
cp _headers public/
