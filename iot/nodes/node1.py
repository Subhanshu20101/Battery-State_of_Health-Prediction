import socket

node1_ip= '172.16.84.83'
node2_ip= '172.16.115.82'
node3_ip= '172.16.122.77'


SOH = {}
cluster_head = ''


def fetchSOH():
    return 100


def serverCH(p):
    # get the hostname
    host = node1_ip # ip of node1
    port = p  # initiate port no above 1024

    server_socket = socket.socket()  # getple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection

    print("Connection from: " + str(address))


    data = conn.recv(1024).decode()
    # SOH[address[0]]=data
    cluster_head = data
    print("from connected user: " + str(data))
    conn.close()


def server_program(p):
    # get the hostname
    host = node1_ip #ip of node1
    port = p  # initiate port no above 1024

    server_socket = socket.socket()  # getple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    # print(type(address[0]))
    print("Connection from: " + str(address))


    data = conn.recv(1024).decode()
    SOH[address[0]]=int(data)
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



p=5000
client_program(node2_ip, p) # ip of the node2
p=6000
client_program(node3_ip,p) # ip of the node3
p=7000

server_program(p) # for node2 to send message
p=9000

server_program(p) # for node3 to send message

SOH[node1_ip]= fetchSOH()

#updating cluster head
serverCH(11000) # for node2 to update CH

print('Cluster head is : '+ cluster_head)
# print(SOH)