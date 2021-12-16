import socket
import random
host = 'local host'
port = 5000



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('', port))

s.listen(1)
  
c, addr = s.accept()

print("CONNECTION FROM:", str(addr))

while True:
    msg=input("Enter a message to send or q to quit :")
    emsg=''
    key=''
    if msg=='q':
        break;
    for i in range(len(msg)):
        a=random.randint(0,100)
        key+=str(a)+','
        emsg+=chr(ord(str(msg[i]))+a)
        
    print('Encrypted message :'+emsg)    
    print('key:'+key[:-1])
    c.send(bytes(emsg+'key'+key,'utf-8'))
    
# disconnect the server
c.close()
