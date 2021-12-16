import socket

host = 'local host'
port = 5000

s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

s.connect(('127.0.0.1', port))

msg = s.recv(1024)

while msg:
    dmsg=''
    
    msg=msg.decode("utf-8") 
    emsg,key=msg.split('key')
    print('Received message:' + emsg)
    print('Received Key:'+key[:-1])
    key=key.split(',')
    
    for i in range(len(emsg)):
        dmsg+=chr(ord(emsg[i])-int(key[i]))
    print('Decrypted Message is :',dmsg)
    msg = s.recv(1024)

# disconnect the client
s.close()
