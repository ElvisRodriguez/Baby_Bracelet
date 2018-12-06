import random
import requests
import socket

HOST = socket.gethostbyname('elvisrodriguez.pythonanywhere.com')

PORT = 443

def generate_hb():
    hb = random.randint(80,160)
    yield hb

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print('Connected to server at {host}'.format(host=HOST))
hb = generate_hb()
message = next(hb)
print('Sending {message}'.format(message=message))
message = message.encode('utf-8')
client_socket.sendall(message)
data = client_socket.recv(1024)
print('Received {data}'.format(data=data))
client_socket.close()
