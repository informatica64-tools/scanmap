#!/usr/bin/env python3

# Import modules
import sys, os, socket

def openPorts(host):
    for i in range(1, 65535):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con = serverSocket.connect_ex((host, i))
        if (con == 0):
            print("Port ==>",i,"is Open")
        serverSocket.close()


f = openPorts(sys.argv[1])


