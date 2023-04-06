import socket

host = socket.gethostbyname(socket.gethostname())
port = 8080


storedValue = "hey , whats up"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete")
    return s

def setupConnection():
    s.listen(1)
    conn, address = s.accept()
    print("Connected to : "+ address[0] + ":" + str(address[1]))
    return conn


def GET():
    reply = storedValue
    return reply 

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply


def dataTransfer(conn):
    # a loop that sends/ recieve data until told not to .
    while True:
        # Recieve the data 
        data = conn.recv(1024)
        data = data.decode('utf-8')
        # split the data such that you separate the command from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage) 
        elif command == 'EXIT':
            print("Our client has left us: (")
            break
        elif command =='KILL':
            print("Oure server is shutting command")
            s.close()
            break
        else:
            reply = 'Unknown command'
        # send the reply back to the client 
        conn.sendall(str.encode(reply))
        print("DATa has been sent")
    conn.close()

s = setupServer()

while True:
    try:
        conn  = setupConnection()
        dataTransfer(conn)
    except:
        break