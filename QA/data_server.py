import socket

HOST = socket.getfqdn()
PORT = 12345

if __name__ == '__main__':
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    print('Listening...')
    server_socket.bind((HOST,PORT))
    server_socket.listen(5)
    while True:
        connection, address = server_socket.accept()
        print('Connected by {addr}'.format(addr=address))
        data = connection.recv(1024)
        data = int(data)
        print('{data} is of type {type}'.format(data=data,type=type(data)))
    connection.close()
