from scapy.all import wrpcap, Ether, IP, UDP
from scapy.all import *
import base64
import random
import string

flag="DRNCUD0G904LT1YT3011ABU1143SAR" #"dc9111{A11_Y0uR_D4tA_4r3_B3l0ng_T0_Us}"

packets=list()
for i in flag:
	payload=''.join(random.choices(string.ascii_uppercase + string.digits, k = ord(i)))

	packets.append(Ether() / IP(dst="127.0.0.1") / UDP(dport=random.randint(1,65535)) / base64.b64encode(bytes(payload,"ascii")))
	packets.append(Ether() / IP(dst="127.0.0.1") / TCP(dport=random.randint(1,65535)) / ' '.join(format(ord(x), 'b') for x in payload ) )
	packets.append(IP(dst="127.0.0.1")/UDP(dport=random.randint(1,65535))/Raw(load=payload))
	packets.append(ARP(op=1, psrc="127.0.0.1", pdst="127.0.0.1"))
	packets.append(Ether() / IP(dst="127.0.0.1", src="127.0.0.1")/TCP(sport=random.randint(1,65535), dport=random.randint(1,65535))/payload)
	packets.append(IP(dst="127.0.0.1")/TCP(sport=random.randint(1,65535), dport=random.randint(1,65535)))
	packets.append(IP(dst="127.0.0.1")/ICMP())
	packets.append(Ether() / IP(dst="127.0.0.1",ttl=(1,4)) )

wrpcap('chall.pcap', packets)
