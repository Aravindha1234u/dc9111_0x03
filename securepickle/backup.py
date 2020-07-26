#!/usr/bin/python3

import pickle
import io
import random 
import codecs
import os,sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 45057))
s.listen(1)
conn, addr = s.accept()
conn.send(b"Welcome to Pickle Shell!\n")
conn.send(b"Lets start the game.\n")
while True:
	try:
		conn.send(b"$ ")
		data={
		"cmd": str(conn.recv(2048),"latin-1")
		}
		if "\\x" not in data['cmd']:
			cmd=pickle.loads(codecs.decode(data['cmd'].encode(), 'base64'))
			if cmd.split()[0] not in ["ls","cat"]:
				a=[].__class__.__base__.__subclasses__()
				random.shuffle(a)
				conn.send(bytes(a,'latin-1'))
			elif cmd.split()[0] in ["ls","cat"]:
				cmd=cmd.replace(";","").replace("&","").replace("|","")
				pickleBuffer = io.BytesIO()
				pickle.dump(cmd,pickleBuffer)
				conn.send(bytes(str(pickleBuffer.getvalue(),"latin-1"),"latin"))
				conn.send(b"\n")
			else:
				break
		else:
			stringbuf= io.StringIO()
			pickleBuffer = io.BytesIO()
			if data['cmd'].find("ls")!=-1 or data['cmd'].find("cat")!=-1:
				cmd=data['cmd'].split("\\x")[-2][2:]
				pickle.dump(cmd,pickleBuffer)
				stringbuf.write(str(pickleBuffer.getvalue(),'latin-1'))
				conn.send(bytes(os.popen(pickle.loads(bytes(stringbuf.getvalue().strip(),'latin-1'))).read(),"latin-1"))
				conn.send(b"\n")
			else:
				raise Exception
	except Exception as e:
		#print(e)
		if str(e) =="Ran out of input":
			conn.send(b"\nOhhh You broke the shell")
			conn.send(b"\n")
			break
		elif data['cmd']=="exit":
			break
		pickleBuffer = io.BytesIO()
		pickled=codecs.encode(pickle.dumps(data['cmd']), "base64").decode()
		conn.send(bytes(pickled,"latin-1"))
		conn.send(b"\n")
conn.send(b"Good Bye!!")
conn.send(b"\n")
conn.close()
s.close()
