import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Waiting for connection...")

conn, addr = s.accept()
print(f"Connected to {addr}")

while True:
    try:
        data = conn.recv(1024).decode()
        if not data: break
        print("Client:", data)
        conn.send(f"ACK: {data}".encode())
    except: break

conn.close()
