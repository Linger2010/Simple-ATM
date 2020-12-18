CONTENTS OF THIS FILE
---------------------

* Introduction
* Requirements
* Using the ATM



INTRODUCTION
------------

Written by: Linger2010

This is an ATM with client and server sides. It is designed to support one bank account and one user. Multiple users are not allowed. 


REQUIREMENTS
------------

The ATM needs to be run with python3.


USING THE ATM
-------------
Run the software on two separate terminals. Use port numbers that are greater than 25000. The server side takes the file name and a port number as the parameters; while the client side needs an additional hostname parameter before the port number. Run the server side first.
The account is initialized with a balance of 100$. The following commands are available: 
1. Checking the balance
2. Depositing money into the account
3. Withdrawing money out of the account
4. Exiting the ATM
Note that for any input from the user, only integers within certain range are allowed. For example, the amount of money that is to be withdrawn cannot exceed the current balance.
After choosing to exit the program, users can start the client-side again, and the balance stays persistent.
To shut down the program, the server-side should be disconnected.

CREDITS
-------------
This is a homework assignment for CSCE 4753 Computer Networks instructed by Dr. Dale Thompson.
