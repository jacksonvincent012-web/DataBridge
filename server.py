import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5000))
server_socket.listen(1)
print("Server is listening on port 5000...")
conn, addr = server_socket.accept()
print(f"connected to {addr}")

with open("received_inventory.csv", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

conn.close()
server_socket.close()
print("File received")
