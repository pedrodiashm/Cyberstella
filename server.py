import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #associa a ip e porta
    s.listen() # escuta
    conn,addr = s.accept() # espera oonexão e retorna um objeto socket e endereço
    with conn:
        print(f"conectado!  {addr}")
        while True:
            data = conn.recv(1024)#recebe dados

            if not data:
                break
            conn.sendall(data) #manda para todas as conexões os dados



1