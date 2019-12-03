#!/usr/bin/env python3

import socket
import time

HOST_LEFT = '192.168.254.11'  # The server's hostname or IP address
HOST_CENTER = '192.168.254.12'  # The server's hostname or IP address
HOST_RIGHT = '192.168.254.13'  # The server's hostname or IP address
HOST_REAR = '192.168.254.14'  # The server's hostname or IP address
PORT = 7142        # The port used by the server
POWER_ON = '01304130413043024332303344363030303103730D'
POWER_OFF = '01304130413043024332303344363030303403760D'

time.sleep(30)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as left:
    left.connect((HOST_LEFT, PORT))
    senddata = bytes.fromhex(POWER_OFF)
    left.send(senddata)
    data = left.recv(1024)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as center:
    center.connect((HOST_CENTER, PORT))
    senddata = bytes.fromhex(POWER_OFF)
    center.send(senddata)
    data = center.recv(1024)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as right:
    right.connect((HOST_RIGHT, PORT))
    senddata = bytes.fromhex(POWER_OFF)
    right.send(senddata)
    data = right.recv(1024)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as rear:
    rear.connect((HOST_REAR, PORT))
    senddata = bytes.fromhex(POWER_OFF)
    rear.send(senddata)
    data = rear.recv(1024)
