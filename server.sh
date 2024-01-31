#!/bin/bash

stop_server () {
        PID=$(lsof -t -i:5000)
        kill -9 "$PID"
}

start_server () {
        nohup /usr/bin/python3 /home/fluffyoctopus/wifi_light/main.py &
}

restart_if_necessary() {
        PID=$(lsof -t -i:5000)
        if [ -z "$PID" ];
        then
                start_server
        else
                exit
        fi

        exit
}

case "$1"
in
restart)
        stop_server
        start_server
        ;;
stop)
        stop_server
        ;;
start)
        start_server
        ;;
alwaysOn)
        restart_if_necessary
        ;;
esac
