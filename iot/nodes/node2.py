import socket

node1_ip= '172.16.121.68'
node2_ip= '172.16.123.74'
node3_ip= '172.16.122.77'

SOH = {}
cluster_head = ''



def fetchSOH():
    return 800

def compareSOH():
    if SOH[node1_ip]>= SOH[node2_ip] and SOH[node1_ip]>= SOH[node3_ip]:
        return node1_ip
    
    if SOH[node2_ip]>= SOH[node1_ip] and SOH[node2_ip]>= SOH[node3_ip]:
        return node2_ip
    
    if SOH[node3_ip]>= SOH[node1_ip] and SOH[node3_ip]>= SOH[node2_ip]:
        return node3_ip



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
    host = node2_ip  #ip of node 2
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





p=5000

server_program(p) # for node1 to send message
# print('server ended')
# print(SOH)
p=7000
client_program(node1_ip, p)  # ip of node1
p=8000
client_program(node3_ip, p)  # ip of node3
p=10000

server_program(p)  # for node3 to send message
SOH[node2_ip]= fetchSOH()

# comparing SOH
cluster_head = compareSOH()
#updating SOH to other nodes
client_program(node1_ip, 11000) #ip of node1
client_program(node3_ip, 12000) #ip of node3

print('Cluster head is : '+ cluster_head)

# print(SOH)
