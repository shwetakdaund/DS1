import threading                                               #provides a way to run multiple threads (concurrently executing tasks) in a Python program.
import datetime
import socket                                                  #provides access to the BSD socket interface, allowing communication between processes over a network.
import time

def send_time(slave_client):                                                     #sending the current time to the server.
    while True:
        slave_client.send(str(datetime.datetime.now()).encode())    #sends the current time to the server. datetime.datetime.now() returns the current date and time, 
                                                                #which is converted to a string, encoded as bytes using .encode(), and then sent over the slave_client socket.
        print("Time sent successfully")
        time.sleep(5)                                             # line pauses the execution of the thread for 5 seconds, ensuring that the time is sent every 5 seconds.

def receive_time(slave_client):                                                 #responsible for receiving the synchronized time from the server.
    while True:
        synchronized_time = datetime.datetime.strptime(slave_client.recv(1024).decode(), "%Y-%m-%d %H:%M:%S.%f")
        # receives data from the server using slave_client.recv(1024), decodes it from bytes to a string using .decode()
        print("Synchronized time at the client is:", synchronized_time)

def initiate_slave_client(port=8080):                                           #sets up the client-side socket and starts the sending and receiving threads.
    slave_client = socket.socket()                                              #creates a new socket object
    slave_client.connect(('127.0.0.1', port))              #connects the slave_client socket to the server running on the local machine (127.0.0.1) on the specified port.
    print("Starting to receive time from server")
    threading.Thread(target=send_time, args=(slave_client,)).start()             #creates a new thread that will execute the send_time function and starts it
    print("Starting to receive synchronized time from server")
    threading.Thread(target=receive_time, args=(slave_client,)).start()          #creates another thread that will execute the receive_time function

if __name__ == '__main__':                                                       #checks whether the script is being run as the main program.
    initiate_slave_client(port=8080)                                             #It calls function, starting the client-side communication.