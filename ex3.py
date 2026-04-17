import socket 

host = 'example.com' 
port = 80 

try : 
    client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
    client_socket.connect((host,port))
    print('server is connected to the port')

    request = 'GET / HTTP/1.1\r\n'
    request+= 'Host: ' + host + '\r\n'
    request+= 'Connection: close \r\n\r\n' 

    client_socket.send(request.encode())
    response = "" 
    while True: 
        data = client_socket.recv(1024)
        if not data:
            break 
        response += data.decode() 
    
    print('---server response---')
    print(response) 

    client_socket.close() 
    print('connection closed ')
except Exception as e:
    print('error: ', e)