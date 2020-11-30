import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("djxmmx.net", 17))
message = b''
s.sendall(message)
data, address = s.recvfrom(1024)
print(data.decode())
