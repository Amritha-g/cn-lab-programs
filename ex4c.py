import socket 

cl_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM ) 

cl_socket.connect(('localhost',8080)) 

while True : 
    msg = input('input the message: ') 
    cl_socket.send(msg.encode()) 
    if msg.lower() == "exit" : 
        break 
    
    data = cl_socket.recv(1024).decode() 
    print('the data receiver from the server: ',data) 

cl_socket.close() 
print('socket is closed ')