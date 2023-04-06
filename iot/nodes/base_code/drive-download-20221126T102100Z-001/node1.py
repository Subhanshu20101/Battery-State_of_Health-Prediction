import socket

# SOH = {'rpi1': 0 , 'rpi2': 0, 'rpi3': 0}
SOH = {}

SERVER = False
CLIENT = True

def fetchSOH():
    return 1000


def server_program(p):
    # get the hostname
    host = '172.16.121.68'
    port = p  # initiate port no above 1024

    server_socket = socket.socket()  # getple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    # print(type(address[0]))
    print("Connection from: " + str(address))


    data = conn.recv(1024).decode()
    SOH[address[0]]=data
    print("from connected user: " + str(SOH[address[0]]))
    conn.close()

def client_program(ip, p):
    host = ip  # ip of the server connecting to ...
    port =  p # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    message= str(fetchSOH())
    client_socket.send(message.encode())
    client_socket.close()

    # message = input(" -> ")  # take input

    # while message.lower().strip() != 'bye':
    #     client_socket.send(message.encode())  # send message
    #     data = client_socket.recv(1024).decode()  # receive response

    #     print('Received from server: ' + data)  # show in terminal

    #     message = input(" -> ")  # again take input

    # client_socket.close()  # close the connection


p=5000
client_program('172.16.123.74', p) # ip of the node2
p=6000
client_program('172.16.122.77',p) # ip of the node3
p=7000

server_program(p) # for node2 to send message
p=9000

server_program(p) # for node3 to send message

print(SOH)