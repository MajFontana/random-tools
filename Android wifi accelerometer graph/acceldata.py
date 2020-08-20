import socket
import numpy
import matplotlib.pyplot
import matplotlib.animation

PORT = 1024
BUFF = 1024
INTERVAL = 1
SIZE = 4000
SAMPINTER = 0.001
LIMIT = (-10, 10)

def op(x):
    return x * 100

data = b""
samps = numpy.zeros(SIZE)
def update(_):
    global data, samps
    data += con.recv(BUFF)
    bound = (len(data) // 8) * 8
    start = max(0, bound - chunk)
    new = numpy.frombuffer(data[start:bound], "f8")
    data = data[bound:]
    if len(new):
        new = vecop(new)
        samps = numpy.concatenate((samps[len(new):], new))
    ax.clear()
    ax.plot(scale, samps)
    ax.set_ylim(LIMIT)

s = socket.socket()
s.bind(("0.0.0.0", PORT))
s.listen(1)
con, addr = s.accept()
s.close()

chunk = SIZE * 8
vecop = numpy.vectorize(op)
scale = numpy.arange(-((SIZE - 1) * (SAMPINTER)), SAMPINTER / 2, SAMPINTER)
fig, ax = matplotlib.pyplot.subplots(figsize=(20, 5))
ani = matplotlib.animation.FuncAnimation(fig, update, interval = INTERVAL)
matplotlib.pyplot.show()

con.shutdown(socket.SHUT_RDWR)
