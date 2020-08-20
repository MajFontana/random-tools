import androidhelper
import time
import socket
import struct
import math

INTERVAL = 0.001
HOST = "192.168.1.36"
PORT = 1024

def readAcc():
    return drd.sensorsReadAccelerometer().result

s = socket.socket()
s.connect((HOST, PORT))

drd = androidhelper.Android()
drd.startSensingTimed(2, 0)
while None in readAcc():
    pass

#oldx = 0
#oldy = 0
#oldacc = [0, 0, 0]
#past = []
win = [[0 for _ in range(10)] for _ in range(3)]
tlast = time.time()
while 1:
    acc = readAcc()
    sm = 0
    for i in range(3):
        win[i].append(acc[i])
        win[i].pop(0)
        mean = sum(win[i]) / len(win[i])
        dev = sum([(samp - mean) ** 2 for samp in win[i]]) / len(win[i])
        sm += dev
    pw = math.sqrt(sm)
    #delta = sum([(acc[i] - oldacc[i]) ** 2 for i in range(3)])
    #oldacc = acc
    #past.append(delta)
    #if len(past) > 10:
        #past.pop(0)
    #pw = sum(past) / len(past)
    #y = acc - oldx + oldy * 0.9
    #oldx = acc
    #acc = y
    #oldy = acc
    #acc -= math.copysign(9.8, acc)
    raw = struct.pack("d", pw)
    try:
        s.sendall(raw)
    except (BrokenPipeError, ConnectionResetError):
        break
    while time.time() - tlast < INTERVAL:
        pass
    tlast += INTERVAL