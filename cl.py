import socket

sv_addr = '127.0.0.1'  
sv_port = 1783        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    txt = input("Input: ")
    client_socket.sendto(txt.encode(), (sv_addr, sv_port))
    
    mod_msg, _ = client_socket.recvfrom(1024)
    print(mod_msg.decode())
