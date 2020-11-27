# Yaling Liu
# Std No. 010945821

import binascii
import struct
import sys

from socket import *

serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('', serverPort))

balance = 100

while 1:

    serverSocket.listen(1)

    unpacker = struct.Struct('I I')

    connectionSocket, addr = serverSocket.accept()
    
    isValid = True
    
    while isValid:

        try:
            data = connectionSocket.recv(unpacker.size)

            unpacket_data = unpacker.unpack(data)

            choice, dollarAmount = unpacket_data

            values = ''
            packer = struct.Struct('I I')

            if choice == 1:
                values = (1, balance)
            elif choice == 2:
                balance += dollarAmount
                values = (2, 1)
            elif choice == 3:
                if balance >= dollarAmount:
                    balance = balance - dollarAmount
                    values = (3, 1)
                else:
                    values = (3, 0)
            else:
                values = (4, 0)

            packed_data = packer.pack(*values)

            connectionSocket.send(packed_data)
 
            if choice == 4:
                
                connectionSocket.close()
                isValid = False
            
        except Exception as ex:
            print('crashed!')
            print(ex.message)
            exit(1)