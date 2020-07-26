#Challenge Name :
	Shark Cry
	
#Challenge Description :
	We had recently undergo a ransomware attack and last week we restored all disk but I as a network analyst, Feel that there is some kind of malicious activity which is going in the background, So taught to run a tcpdump and got a PCAP file which has been attached below. Which has some random data frame requests which is transmistted within localhost subnet and to random port. I see some wired data transfer but all I can say is they follow some kind of pattern request where length of the data is also different and also nothing is clear text readable. Please help to remove this ransomware, Please dont tell me to pay ransom and get the key to resolve this.
	
	Hint : 
		[Free] : No of different packets might help you to decrypt.
		[20]   : Check the pattern and length of the data
	
# Challenge Caterogy : Forencisc

# Difficult level : Easy

# Flag : DC9111{A11_Y0UR_D4TA_4R3_B3L0NG_T0_US} or DC9111A11Y0URD4TA4R3B3L0NGT0US

# File : 

#Writeup:

* First of all we have fix pcap file header change DD CC BB AA to D4 C3 B2 A1. then open file in wireshark and analyse
* There are totally 7 different packet with order and repetation, they common data and each packet is either encrpyted in base64 or binary or clear text ascii
* but when you check tcp packet, its payload length seems to be kind of sequence of numbers
* scrape it and put them under ascii to text and you will get "DRNCUD0G904LT1YT3011ABU1143SAR"
* This is a railfence cipher with rows to 7 (From hint)
* BOOM you will get the flag
