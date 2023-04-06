import socket

# SOH = {'rpi1': 0 , 'rpi2': 0, 'rpi3': 0}
SOH = {}

SERVER = True
CLIENT = False

def fetchSOH():
    return 500

def client_program(ip, p):
    host = ip  # ip of the server connecting to ...
    port = p  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    message= str(fetchSOH())
    client_socket.send(message.encode())
    client_socket.close()


def server_program(p):
    # get the hostname
    host = '172.16.122.77'
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




    # while True:
    #     # receive data stream. it won't accept data packet greater than 1024 bytes
    #     data = conn.recv(1024).decode()
    #     if not data:
    #         # if data is not received break
    #         break
    #     print("from connected user: " + str(data))
    #     data = input(' -> ')
    #     conn.send(data.encode())  # send data to the client instance
    # # look closely. The bind() function takes tu

    # conn.close()  # close the connection

p=6000
server_program(p) # for node1 to send message
# print('server ended')
# print(SOH)
p=8000
server_program(p) # for node2 to send message
p=9000

client_program('172.16.121.68', p) #ip of node1
p=10000
client_program('172.16.123.74', p) #ip of node2

print(SOH)