import socket

IP = 'localhost'
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
file = 'new_file.txt'
with open(file, 'w') as f: #open file
    while True:
        # receive
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            f.close()
            break
        # write data to a file
        f.write(data)

s.close()
