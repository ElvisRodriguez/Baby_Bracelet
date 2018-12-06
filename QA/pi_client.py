import random
import requests
import socket

WEBSITE = 'elvisrodriguez.pythonanywhere.com'
HOST = socket.gethostbyname(WEBSITE)

PORT = 443

def generate_hb():
    hb = random.randint(80,160)
    yield hb

print('Sending...')
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print('Connected to server at {host}'.format(host=HOST))
hb = generate_hb()
header = 'GET / HTTP/1.1\r\nHost: {host}\r\n\r\n'.format(host=HOST)
message = str(next(hb))
print('Sending {message}'.format(message=message))
header = header.encode('utf-8')
message = message.encode('utf-8')
client_socket.send(header)
client_socket.sendall(message)
data = client_socket.recv(1024)
print('Received {data}'.format(data=data))
client_socket.close()
