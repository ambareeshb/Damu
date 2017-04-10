from socket import *
import time
import threading
from termcolor import colored

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('10.2.0.147',serverPort))
print "\n--Damu 1.0 chat_server--\n"
clientAddress=('0.0.0.0',00000)
def listen_on_socket():
	while 1:
		global clientAddress
		message,clientAddress = serverSocket.recvfrom(serverPort)		       
		#print "[DEBUG] client address", clientAddress
		print "\r"
		print colored((clientAddress[0])+':','blue'),colored(message,'yellow')
	

#Starting thread for listening on socket on 12000
socket_listen_thread = threading.Thread(target=listen_on_socket)
socket_listen_thread.start()

while 1:
	global clientAddress
	replyMessage=raw_input('')	
	#print "[DEBUG] client address", clientAddress
 	if clientAddress[0] == '0.0.0.0':
		print colored("Listen Damu you have no one...really no one.. to chat with",'red')
	
	else:
		serverSocket.sendto(replyMessage,clientAddress)
	



