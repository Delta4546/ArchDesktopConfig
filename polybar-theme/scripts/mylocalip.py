#!/usr/bin/python3
#-*- coding:utf-8 -*-

import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)
