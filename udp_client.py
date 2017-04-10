from socket import *
import time
import threading
from termcolor import colored

serverName = '10.2.0.147'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
print "\n---Damu 1.0 chat_client---\n"
serverAddress = (serverName,serverPort)
def listen_on_socket():
	while 1:
		#2048 is the buffer size on the below code recvfrom(2048)
	 	replyMessage, serverAddress = clientSocket.recvfrom(2048)
#		print colored('[DEBUG] server address is'+(serverAddress[0]),'grey')
		print colored((serverAddress[0])+ ':','blue'),colored(replyMessage,'yellow')

#Start a thread for listening on sockcet (socket number is selected by UDP)
socket_listen_thread = threading.Thread(target=listen_on_socket)
socket_listen_thread.start()

while 1:
	global serverAddress
	message = raw_input('')
	clientSocket.sendto(message,serverAddress)


