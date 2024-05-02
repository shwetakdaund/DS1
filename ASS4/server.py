from dateutil import parser                             #parse datetime strings into datetime objects.
import threading
import datetime
import socket                                           #networking communication.
import time

client_data = {}                 #empty dictionary that will be used to store data about connected clients, such as their clock time and time difference from the server.

def start_receiving_clock_time(connector, address): #receives clock time data from a client.  takes connector (the connection socket with the client) and address (the address of the client) as parameters.
    while True:
        clock_time = parser.parse(connector.recv(1024).decode())    #receives clock time data from the client, decodes it, and parses it into a datetime object using the parser from dateutil
        clock_time_diff = datetime.datetime.now() - clock_time      #calculates the time difference between the server's current time and the received clock time from the client.
        client_data[address] = {"clock_time": clock_time, "time_difference": clock_time_diff, "connector": connector}
        #updates the client_data dictionary with information about the client, including its clock time, time difference from the server, and the connection socket.
        time.sleep(5)

def start_connecting(master_server):                    # accepts connections from clients
    while True:
        master_slave_connector, addr = master_server.accept()
        client_address = f"{addr[0]}:{addr[1]}"
        threading.Thread(target=start_receiving_clock_time, args=(master_slave_connector, client_address)).start()
        print(f"Client connected from address {client_address}")
        
def synchronize_all_clocks():
    while True:
        if len(client_data) > 0:
             avg_clock_diff = sum((client['time_difference'] for client in client_data.values()), datetime.timedelta()) / len(client_data)
             for client in client_data.values():
                synchronized_time = datetime.datetime.now() + avg_clock_diff
                try:
                    client['connector'].send(str(synchronized_time).encode())
                except Exception as e:
                    print(f"Error sending synchronized time to {client['address']}: {e}")
        time.sleep(5)

def initiate_clock_server(port=8080):
    master_server = socket.socket()
    master_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    master_server.bind(('', port))
    master_server.listen(10)
    print("Clock server started...")
    threading.Thread(target=start_connecting, args=(master_server,)).start()
    threading.Thread(target=synchronize_all_clocks).start()

if __name__ == '__main__':
    initiate_clock_server()