import random
import socket

HOST = socket.gethostbyname('elvisrodriguez.pythonanywhere.com')
PORT = 11203

def generate_hb():
    hb = random.randint(80,160)
    yield hb

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
hb = generate_hb()
hb = str(next(hb))
hb = hb.encode('utf-8')
client_socket.sendall(hb)
client_socket.close()
