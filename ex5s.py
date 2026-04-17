import socket 

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

server_socket.bind(('127.0.0.1',9999)) 

server_socket.listen(1) 
print('the server socket is waiting for the connection')

conn , addr = server_socket.accept() 
print('connected to :' , addr) 

while True : 
    data = conn.recv(1024).decode() 
    print('client: ' , data)
    if data.lower() == "quit" :
        break

    msg = input('server: ')
    conn.send(msg.encode())

    if msg.lower() == "quit" : 
        break 
conn.close() 
server_socket.close() 
print('the connection was closed ')