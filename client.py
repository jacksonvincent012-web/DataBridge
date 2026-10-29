import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))
with open("inventory.csv", "rb") as f:
    file_bytes = f.read()
    client_socket.sendall(file_bytes)
    client_socket.close()
    print("File sent successfully!")
