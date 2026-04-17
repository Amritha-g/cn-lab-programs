# CN Lab 8 - RARP Server
# Converts MAC address into IP address using UDP

import socket

# Step 1: RARP table (MAC -> IP mapping)
rarp_table = {
    "6A:08:AA:C2": "165.165.80.80",
    "8A:BC:E3:FA": "165.165.79.1"
}

# Step 2: create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 3: bind socket
server.bind(("127.0.0.1", 1309))

print("RARP Server is running...")

# Step 4: communication loop
while True:

    # receive MAC address from client
    data, addr = server.recvfrom(1024)
    mac = data.decode().strip()

    # find IP address
    ip = rarp_table.get(mac, "Not Found")

    # send IP address to client
    server.sendto(ip.encode(), addr)