import socket

HOST = "127.0.0.1"  # ip e porta do serve
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #conecta no server
    s.sendall(b"Hello, world") #envia dados
    data = s.recv(1024) #recebe dados

print(f"Received {data!r}")