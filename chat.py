import socket, random, threading, sys

host = "localhost"
port = random.randint(4000,5000)

class Server(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		
		self.host = "localhost"
		self.port = random.randint(2000,3000)
		
		print("Listening on {0}:{1}".format(self.host,self.port))
		self.serverSocket = socket.socket()
		self.serverSocket.bind((self.host, self.port))
		self.serverSocket.listen()

	def run(self):	
		while True:
			conn, addr = self.serverSocket.accept()
			print('Connected by {0}'.format(addr))
			threading.Thread(target=self.handleConnection, args=(conn, addr)).start()
				
		self.serverSocket.close()

	def handleConnection(self, conn, addr):
		with conn:
			data = conn.recv(1024)
			if data:
				print("{0} Says: {1}".format(addr,data.decode("utf-8")))
				conn.sendall(data)

class Client(threading.Thread):    
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):               
        sent=self.sock.send(msg.encode('utf-8'))           
        #print "Sent\n"
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            host= input("Enter the hostname\n>>")            
            port=int(input("Enter the port\n>>"))
        except EOFError:
            print("Error")
            return 1
        
        print ("Connecting\n")
        s=''
        print(host)
        self.connect(host,port)
        print ("Connected\n")
        srv=Server()
        srv.daemon=True
        print ("Starting service")
        srv.start()
        while 1:            
        
            msg=input('>>')
            if msg=='exit':
                break
            if msg=='':
                continue
           
            self.client(host,port,msg)
        return(1)

myserver = Server()
myclient = Client()
myserver.start()

while(True):
	print("1) Add connection")
	print("2) List connections")
	
	try:
		ch = int(input("Choice >"))
	except ValueError: continue

	if ch == 1:
		peer_ip = input("IP>")
		peer_port = input("PORT>")
		connections.append((peer_ip, int(peer)))

	if ch == 2:
		for i, connection in enumerate(connections): print(str(i+1))
		try:
			talkto = input("Choice >")
			msg = input("Message >")
			clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			clientSocket.connect(connections[int(talkto)-1])
			clientSocket.sendall(bytes(msg, "utf-8"))			
		except (IndexError, ValueError):
			print("Input Error")
