# coding: utf-8
#
# 13/03/2020

import socket
import threading
import time


host, port = ('', 9000)

#Creat a socket:

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

tello_addresse = ('192.168.10.1', 8889)

