
import socket
import sys

ms = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    ms.bind(('',1234))
except socket.error:
    print("Failed to bind")
    sys.exit()

ms.listen (5)

while True:
    conn, addr = ms.accept()
    data = conn.recv(1000)
    print("Got a request!")
    if not data:
        break

conn.sendall(data)
    
conn.close()
ms.close()
