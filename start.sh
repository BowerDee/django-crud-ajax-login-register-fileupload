#!/bin/bash
ps -aux | grep 'python manage.py runserver' | grep -v grep | cut -c 10-16 | xargs kill -9
nohup python manage.py runserver 127.0.0.1:8081 > ./djo.out 2>&1 &
