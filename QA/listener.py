import socket

HOST = '127.0.0.1'
PORT = 5000
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listen_data(host=HOST, port=PORT, s=SOCKET):
    print('Listening...')
    s.bind((host,port))
    s.listen(5)
    connection, address = s.accept()
    print('Connected by {addr}'.format(addr=address))
    while True:
        data = connection.recv(1024)
        if not data:
            print(str(data))
            yield data
    connection.close()

if __name__ == '__main__':
    listen_data()
