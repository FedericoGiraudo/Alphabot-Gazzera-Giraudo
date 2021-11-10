import socket as sck
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(('192.168.0.122', 5000))
while True:
    stringa = input("scrivi un messaggio: ")
    s.sendall(stringa.encode())
    
sock.close()   