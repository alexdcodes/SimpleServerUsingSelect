import socket, select

s = socket.socket()

z = socket.gethotname()
port = 1234
s.bind((z, port))

s.isten(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r in s:
            c, addr = s.accept()
            print("Got Connection from", addr)
            inputs.append(c)
        else:
            try:
                dd = r.recv(1024)
                disconnected = not dd
            except socket.error
                disconnceted = True

            if disconnected:
                print(r.getpeername(), 'disconeccted')
                inputs.remove(r)
            else
                print(dd)