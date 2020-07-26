#Challenge Name : Pickle Shell

#Categorie : Pwn

#Description:
You know all better than me just challenge name describes everything, if not google it

#Flag:
dc1111{p1Ck1iNg_s0m3_PiCklEs}

#Connection 
nc 52.147.195.39 45057

#writeup

* On connecting to the netcat connection, it says **Welcome to Pickle Shell!** which denotes were are on a shell.

* when we try regular commands of linux machine it return on base64 string. when we decode it, **** some Garage value and which what command we tried.

* From title lets decode with pickle base64 we get a hex string with delimiter as \x **\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x02ls\x94.**

* lets see which if we give base64 pickle string into to the shell and it return same string, as what we have made one with pickle decrypt 

* Lets make pickle according to its returning pickle string and lets test with this **\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x02ls\x94.** 

* And its executes the command and found a **flag.txt** out there, lets modify our command and pickle hex it and lets sent it.

* Sending string **\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00\x8c\x02cat flag.txt\x94.** and BOOMMM we get the flag **dc1111{p1Ck1iNg_s0m3_PiCklEs}**
