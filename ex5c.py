import socket 

client_server = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 

client_server.connect(('127.0.0.1',9999)) 

while True:
    msg = input('client: ') 
    client_server.send(msg.encode()) 
    if msg.lower() == "quit":
        break 

    data = client_server.recv(1024).decode() 
    print('server: ' , data) 
    if data.lower() == "quit" : 
        break 

client_server.close() 
print('the server is closed ')  