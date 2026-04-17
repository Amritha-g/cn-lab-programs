# CN Lab 8 - RARP Client
# Sends MAC address and receives IP address

import socket

# Step 1: create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 2: get MAC address from user
mac = input("Enter the Physical Address (MAC): ")

# Step 3: send MAC to server
client.sendto(mac.encode(), ("127.0.0.1", 1309))

# Step 4: receive IP address
data, addr = client.recvfrom(1024)

# Step 5: display result
print("The Logical Address (IP) is:", data.decode().strip())

# Step 6: close socket
client.close()