import socket
from threading import Thread

IP = 'localhost'
PORT = 50001

class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        # thread initialized

    def run(self):
        filename = 'file.txt'
        f = open(filename, 'r')
        while True:
            line = f.read(1024)
            while (line):
                self.sock.send(line)
                line = f.read(1024)
            if not line:
                f.close()
                self.sock.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    # listen and wait for connections
    tcpsock.listen(5)
    (conn, (ip, port)) = tcpsock.accept()
    # when we receive a connection
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
