import threading
import time
import random

import socket
import sys
import re

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #read in port num from cmd line
    tsPort = int(sys.argv[1])

    server_binding = ('', tsPort)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    data_from_client = csockid.recv(1024)
    query = data_from_client.decode('utf-8')
    values = query.split('\n')
    #print(values)

    #Read dnsrs data store in dictionary
    content_array = []
    data = open('PROJI-DNSTS.txt') 
    for line in data:
        temp = line.split(' ')
        content_array.append(temp)

    #print(content_array)
    #Data look up time ^0^
    data_to_send_client = []
    
    
    for i in range(0, len(values)):
        for j in range(0, len(content_array)):
            if values[i] in content_array[j][0]:
                word = content_array[j][0] + " " + content_array[j][1] + " " + content_array[j][2]
                data_to_send_client.append(word)             
            else:
               if values[i] not in content_array[j][0] and values[i] is '':
                    data_to_send_client.append(values[i])
            


                
                
    print(data_to_send_client)
    #print("This is out:", data_to_send_client)
    outward = data_to_send_client[0] + '\n'
    for i in range(1, len(data_to_send_client)):
        outward = outward + data_to_send_client[i] + '\n'
    print("This is outward:" ,outward)
    csockid.send(outward.encode('utf-8'))
server()
