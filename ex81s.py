import socket

arp_table = {
    '165.165.80.80' : '6A:7E:84:8A' , 
    '165.165.79.1' : '7B:BU:K8:P0' 
}

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

server_socket.bind(('127.0.0.1', 5604))

server_socket.listen(1) 
print('connecting server') 

conn , addr = server_socket.accept()
print('connected to: ', addr)

while True:
    ip = conn.recv(1024).decode().strip() 
    if not ip :
        break 

    mac = arp_table.get(ip,'not found')
    conn.send((mac + '\n').encode())

conn.close() 
server_socket.close()
print('server is closed ')