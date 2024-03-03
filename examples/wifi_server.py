import socket

HOST = "10.0.0.48" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

#alternatively, HOST = socket.gethostbyname(socket.gethostname())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
	print("Server is starting\n")
	
    try:
        while True:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
			connected = True
			while connected:
				data = client.recv(1024)      # receive 1024 Bytes of message in binary format
				if data != b"":
					print(data)     
					client.sendall(data) # Echo back to client
			client.close()
			print("Just closed a connection\n")
    except: 
        print("Closing socket")
        s.close()    