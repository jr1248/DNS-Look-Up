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
    #print('INITIAL VALUES TABLE: ', values)

    #Read dnsrs data store in 2D array
    content_array = []
    data = open('PROJI-DNSTS.txt') 
    for line in data:
        temp = line.split(' ')
        content_array.append(temp)
        
    
    #print("content array: ", content_array)
    #Data look up time ^0^
    data_to_send_client = []
    error = [] 
    #If there, then append to data to send to client
    for j in range(0, len(content_array)):
        for i in range(0, len(values)):
            if values[i] not in content_array[j]:
                error.append(values[i])
                print('INITIAL ERROR, ', error)
                print('DNS: ', content_array[j][0], '\nVALUE: ', values[i])
            else:
               print('print good values: ', values[i])
               good = content_array[j]
               data_to_send_client.append(good)
               print("output array: ", data_to_send_client)
                
            print("end for1")
        print("end for2")
    print("end for3")
 
    
 
    error = list(dict.fromkeys(error))
    for i in range(0, len(error)):
        error[i] = error[i] + " " + "-" + " " + "ERROR:HOST NOT FOUND"
    print('bad list', error)
      
              
    '''            
    print(data_to_send_client)
    #print("This is out:", data_to_send_client)
    outward = data_to_send_client[0] + '\n'
    for i in range(1, len(data_to_send_client)):
        outward = outward + data_to_send_client[i] + '\n'
    print("This is outward:" ,outward)
    csockid.send(outward.encode('utf-8'))
    '''
server()
