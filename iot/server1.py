import socket
import threading

HEADER = 64
PORT = 5000
# SERVER =  '172.16.142.222'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT='utf-8'  
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
 
def handle_client (conn, addr):
    print(f'[New conncection] {addr}. ')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(float(msg_length))
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected= False
            print(f"[{addr}] {msg}")
            conn.send("msg recienve".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f" [Listeneing] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active connection] {threading.activeCount()-1}")


print("[STARTING],server is starting")
start()