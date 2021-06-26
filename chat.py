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
	def __init__(self):
			threading.Thread.__init__(self)
			
			self.host = "localhost"
			self.port = random.randint(2000,3000)       

    def run(self):
    		msg = input("Message >")
			clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			clientSocket.connect(connections)
			clientSocket.sendall(bytes(msg, "utf-8"))
			while True:
			conn, addr = self.serverSocket.accept()
			print('Connected to {0}'.format(addr))
			threading.Thread(target=self.handleConnection, args=(conn, addr)).start()

		except (IndexError, ValueError):
			print("Input Error")


        self.clientSocket.close()


myserver = Server()

myserver.start()

connections = []

while(True):
	print("1) Add client")
	print("2) List of clients connected to the server")
	
	try:
		ch = int(input("Choice >"))
	except ValueError: continue

	if ch == 1:
		client_ip = input("IP>")
		client_port = input("PORT>")
		connections.append((client_ip, int(client)))

	if ch == 2:
		for i, connection in enumerate(connections): print(str(i+1))
		try:
			talkto = input("Choice >")
			myclient = Client()
			myclient.start()

		
		except (IndexError, ValueError):
			print("Input Error")
