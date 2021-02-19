import threading
import time
import random

import socket
import sys

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #read in port num from cmd line
    rsPort = int(sys.argv[1])

    server_binding = ('', rsPort)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    data_from_client = csockid.recv(200)
    print(data_from_client.decode('utf-8'))
    
    """
    #recieve message from client
    look_up = []
    while True:
        csockid, addr = ss.accept()
        print ("[S]: Got a connection request from a client at {}".format(addr))
        data_from_client = csockid.recv(200)
        while data_from_client:
            look_up.append(data_from_client.decode('utf-8'))
            data_from_client = csockid.recv(200)
        break
    
    print(look_up)
    #lookup
    data = open('PROJI-DNSRS.txt') 
    content_array = []
    for line in data:
        content_array.append(line.split(' '))

    out = []
    for i in range(0, len(look_up)):
        for j in range(0, len(content_array)):
            if look_up[i] == content_array[j][0]:
                word = content_array[j][0] + " " + content_array[j][1] + " " + content_array[j][2]
                out.append(word)
            elif look_up[i] != content_array[j][0]:
                out.append(look_up[i])
                if 'NS' in content_array[j][2]:
                    out.append(content_array[j])

                
    #print("This is out:", out)
    #outward = out[0] + '/n'
    #for i in range(1, len(out)):
        #outward = outward + out[i] + '\n'
    #print("This is outward:" ,outward)
    """
    


         
    
    
   
        

    # send a intro message to the client.  
    #msg = "Welcome to CS 352!"
    #csockid.send(msg.encode('utf-8'))


server()
