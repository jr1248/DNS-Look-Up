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
    tsPort = int(sys.argv[3])

    # connect to the server on local machine
    server_binding = (rsHostName, rsPort)
    cs.connect(server_binding)

    #Read HNS file and send data over
    data = open('PROJI-HNS.txt')
    info = data.read()
    infoL = info.lower()
    cs.sendall(infoL.encode('utf-8'))

    # Receive data from the server
    data_from_server=cs.recv(1024)
    response = data_from_server.decode('utf-8')
    recieved = response.split('\n')
    
    arr = []
    for i in range(0,len(recieved)):
        if len(recieved[i]) > 1:
            arr.append(recieved[i].split(' '))
   
    #print(arr)
    result = open('RESOLVED.txt', 'a')

    send_to_tsServer = []
    for i in range(0, len(arr)):
        if 'A' in arr[i][2]:
            word = arr[i][0] + " " + arr[i][1] + " " + arr[i][2] + "\n"
            result.write(word)
        if '-' in arr[i][2]:
            tsWord =  arr[i][0] + " " + arr[i][1] + " " + arr[i][2] + " " + arr[i][3] + "\n"
            send_to_tsServer.append(tsWord)
   
    
    data_ts = []
    tsHostName = ''
    fin_arr = []
    for i in range(0, len(send_to_tsServer)):
        data_ts.append(send_to_tsServer[i].split(' '))
        tsHostName = data_ts[i].pop(1);
        fin_arr.append(data_ts[i][0]);

    #print(data_ts)
    #print(fin_arr)

    to_ts = '\n'.join(fin_arr)
    #print(to_ts)
    cs.close()

    if to_ts != '':
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to the server on machine to ts
        sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        bind_to = (tsHostName, tsPort)
        sc.connect(bind_to)
        sc.send(to_ts.encode('utf-8'))
        # Receive data from the server
        data_from_ts=sc.recv(1024)
        resp = data_from_ts.decode('utf-8')
        rec = resp.split('\n')
        arr_ts = []
        print(rec)

        for i in range(0,len(rec)):
            if len(rec[i]) > 1:
                arr_ts.append(rec[i].split(' '))
        print(arr_ts)
        """
        send_to_tsServer = []
        for i in range(0, len(arr_ts)):
            if 'A' in arr_ts[i][2]:
                word_ts = arr_ts[i][0] + " " + arr_ts[i][1] + " " + arr_ts[i][2] + "\n"
                result.write(word_ts)
          """
        
        result.close()

        





    # close the client socket
    #cs.close()
    exit()

client()