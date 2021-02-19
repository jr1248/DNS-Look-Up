import threading
import time
import random

import socket
import sys



def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # read in cmd line arguements 
    rsHostName = sys.argv[1]
    rsPort = int(sys.argv[2])

    # connect to the server on local machine
    server_binding = (rsHostName, rsPort)
    cs.connect(server_binding)

    #Read HNS file and send data over
    data = open('PROJI-HNS.txt')
    line = data.readline().strip()
    lineL = line.lower()
    cs.sendall(lineL.encode('utf-8'))
    while line != '':
        line = data.readline().strip()
        lineL = line.lower()
        cs.sendall(lineL.encode('utf-8'))
        


    # Receive data from the server
    #data_from_server=cs.recv(1024)
    #response = data_from_server.decode('utf-8')
    #print(response)

    # close the client socket
    #cs.close()
    exit()

client()