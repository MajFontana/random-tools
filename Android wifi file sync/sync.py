import socket
import os
import time

TARGET = "hello.py"
PORT = 1024
DELAY = 0.2
TIMEOUT = 3

def cmd(code, response=False):
    data = bytes(code, "utf-8")
    if not response:
        con.sendall(data)
    if con.recv(len(data)) != data:
        raise ValueError("Invalid response")

def send(txt):
    data = bytes(txt, "utf-8") + b"\x17"
    con.sendall(data)

name = os.path.basename(TARGET)
s = socket.socket()
s.bind(("0.0.0.0", PORT))
s.listen(1)
con, addr = s.accept()
con.settimeout(TIMEOUT)

last = None
while True:
    mtime = os.path.getmtime(TARGET)
    
    if last != mtime:
        os.system("cls")
        print("Transmitting ...")
        with open(TARGET, "r") as f:
            text = f.read()
        cmd("D")
        send(name)
        send(text)
        last = mtime
        print("Storing ...")
        cmd("A", True)
        
        os.system("cls")
        print("File synced")
    else:
        cmd("P")
        
    time.sleep(1)
