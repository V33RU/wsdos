#!/usr/bin/env python3
import sys
import socket
from websocket import create_connection, WebSocket

#ws = create_connection("ws://echo.websocket.org/")
#print("Sending 'Hello, World'...")
#ws.send("Hello, World")
#print("Sent")
#print("Receiving...")
#result =  ws.recv()
#print("Received '%s'" % result)
#ws.close()

def main(argv):
    ipAddress = argv[0]
    count = int(argv[1]);
    conn_count = 0
    ws = []
    wsUrl = "ws://"+ipAddress
    while count > 0:
        ws.append(create_connection(wsUrl,   sslopt={"check_hostname": False},))
        #ws.append(create_connection("ws://echo.websocket.org/", sockopt=((socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),)))
        count = count - 1;
        print("connection established = " + str(conn_count))
        conn_count = conn_count + 1
    for soc in ws:
        soc.close()
        
# wsdos.py <ipAddr> <count>  
if __name__ == "__main__":
    #websocket.enableTrace(True)
    main(sys.argv[1:])
    #while(True):
    #    continue
