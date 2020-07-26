from pwn import *
r=remote("52.147.195.39","45057")
r.recv()
r.recv()
r.recv()
r.close()
