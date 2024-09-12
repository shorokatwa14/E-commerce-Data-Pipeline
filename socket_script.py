import socket
import time

# Configuration
host = 'localhost'
port = 9999
file_path = "/home/shorokatwa14/Documents/SIC_Spark_Mini/large_inventory.json"  

# Create a socket and bind it to the address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on port {port}")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    with open(file_path, 'r') as file:
        for line in file:
            conn.sendall(line.encode('utf-8'))  # Encode each line to bytes
            time.sleep(1)  # Simulate streaming by waiting 1 second between sends
finally:
    conn.close()
    server_socket.close()
