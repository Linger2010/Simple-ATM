# Yaling Liu
# Std No. 010945821

import binascii
import struct
import sys

from socket import *

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
    
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

while 1:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawl")
    print("4. Exit")

    isValid = False
    choice = 0

    while not isValid:
        try:
            choice = int(input("Your choice: "))
            if choice < 1 or choice > 4:
                print("Choice must be between 1 and 4. Try again.")
            else:
                isValid = True
        except ValueError:
            print("Choice must be an integer. Try again.")


    packer = struct.Struct('I I')
    packed_data = ''

    if choice == 1:
        # Check Balance
        values = (1, 0)
        packed_data = packer.pack(*values)
    elif choice == 2:
        # Deposit
        isValidDollarAmount = False
        dollarAmount = 0
        while not isValidDollarAmount:
            try:
                dollarAmount = int(input("The Amount to Deposit($): "))
                if dollarAmount < 0:
                    print("The amount of dollars must be positive. Try again.")
                else:
                    isValidDollarAmount = True
            except ValueError:
                print("The amount of dollars must be an integer. Try again.")
                continue

        values = (2, dollarAmount)
        packed_data = packer.pack(*values)
 
    elif choice == 3:
        # Withdrawl
        isValidDollarAmount = False
        dollarAmount = 0
        while not isValidDollarAmount:
            try:
                dollarAmount = int(input("The Amount to Withdrawl($): "))
                if dollarAmount < 0:
                    print("The amount of dollars must be positive. Try again.")
                else:
                    isValidDollarAmount = True
            except ValueError:
                print("The amount of dollars must be an integer. Try again.")
                continue
                
        values = (3, dollarAmount)
        packed_data = packer.pack(*values)
    else:
        values = (4, 0)
        packed_data = packer.pack(*values)
        #exit(1)

    try:
        clientSocket.send(packed_data)
    except(RuntimeError, TypeError, NameError):
        print('Crashed!')
        exit(1)
        

    unpacker = struct.Struct('I I')

    data = clientSocket.recv(unpacker.size)
    unpacked_data = unpacker.unpack(data)
    choice, flag = unpacked_data

    if choice == 1:
        print("Balance: ", flag, ("$."))
    elif choice == 2:
        if flag > 0:
            print("Deposited Succeeded.")
    elif choice == 3:
        if flag > 0:
            print("Withdrawl Succeeded.")
        else:
            print("Overdraft occurred. Withdrawl failed.")
    else:
        clientSocket.close()
        exit(1)
            
     
        
