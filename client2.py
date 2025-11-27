import socket

HOST = "127.0.0.1"
PORT = 65432

class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        MSGEN = len(bin(msg))
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(bin(msg[totalsent:]))
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)



client = MySocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
client.connect(HOST, PORT)

client.mysend("yoyoyo!")



