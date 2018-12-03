import socket

HOST = socket.gethostname()
PORT = 5000

def listen_data(host=HOST, port=PORT):
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Listening...')
    SOCKET.bind((host,port))
    SOCKET.listen()
    while True:
        connection, address = SOCKET.accept()
        print('Connected by {addr}'.format(addr=address))
        data = connection.recv(1024)
        if not data:
            print(str(data))
            yield data
    connection.close()

if __name__ == '__main__':
    listen_data()
