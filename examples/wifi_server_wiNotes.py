import socket

HOST = "10.0.0.48" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

#alternatively, HOST = socket.gethostbyname(socket.gethostname())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
	print("Server is starting\n")
	
    try:
        while 1:
            client, clientInfo = s.accept() # waits for a new connection from a client
			# when it gets connects, it returns a nested tuple:
			# clientobj, clientInfo. And clientInfo is also a tuple: 
			# clientInfo: ipaddress and port of client 
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)     
                client.sendall(data) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()    