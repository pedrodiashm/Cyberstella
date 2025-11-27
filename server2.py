import socket
PORT = 61432
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))


