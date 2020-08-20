import socket
import os

HOST = "192.168.1.24"
PORT = 1024
BUFF = 1024
DIR = "/storage/emulated/0/synced/"

def wait():
    data = cli.recv(BUFF)
    cli.sendall(data)
    return str(data, "utf-8")

data = b""
def recv():
    global data
    while not b"\x17" in data:
        data += cli.recv(BUFF)
    first, data = data.split(b"\x17", 1)
    return str(first, "utf-8")

def resp(code):
    data = bytes(code, "utf-8")
    cli.sendall(data)

cli = socket.socket()
cli.connect((HOST, PORT))
while True:
    cmd = wait()
    if cmd == "D":
        name = recv()
        text = recv()
        path = os.path.join(DIR, name)
        with open(path, "w") as f:
            f.write(text)
        resp("A")
