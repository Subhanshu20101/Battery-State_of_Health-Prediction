import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
text = "Hello, World!"
mysocket.bind(('192.168.0.114', 8080))
mysocket.listen(5)
(client, (ip,port)) = mysocket.accept()
print(client, port)
client.send(b"knock knock knock, I'm the server")
data = client.recv(buffer_size)
print(data.decode())
mysocket.close()