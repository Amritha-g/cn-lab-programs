# arp 
import socket 

client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 

client_socket.connect(('127.0.0.1',5604))

ip = input('ip:')
client_socket.send((ip + '\n').encode())

mac = client_socket.recv(1024).decode()
print('mac address: ',mac) 

client_socket.close()
print('the conncetion is closed ')

