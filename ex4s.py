import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server_socket.bind(('localhost',8080)) 

server_socket.listen(1)
print('the server is waiting for the connection ') 

conn , addr = server_socket.accept() 
print('connected to : ' , addr ) 

while True : 
    data = conn.recv(1024).decode() 
    if not data:
        break
    print('data received from client: ' , data) 
    conn.send(data.encode())

conn.close() 
server_socket.close() 
print('the server has been closed ')