#/usr/bin/python

import socket

host = ''
port = ''

pin = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.recv(1024)

while True:
	print '[+] Sending: ' + str(pin)
	s.sendall(str(pin) + '\n')
	data = s.recv(1024)
	print data
	pin += 1
