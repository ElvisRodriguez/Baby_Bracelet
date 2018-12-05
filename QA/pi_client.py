import random
import socket

HOST = socket.gethostbyname('elvisrodriguez.pythonanywhere.com')

PORT = 80

def generate_hb():
    hb = random.randint(80,160)
    yield hb

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print(HOST)
client_socket.settimeout(10)
client_socket.connect((HOST, PORT))
client_socket.settimeout(None)
print('Connected to server at {host}'.format(host=HOST))
hb = generate_hb()
hb = str(next(hb))
hb = hb.encode('utf-8')
client_socket.sendall(hb)
data = client_socket.recv(1024)
print('Received {data}'.format(data=data))
client_socket.close()
