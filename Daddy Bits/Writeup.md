#Challenge Name : Daddy Bits

#Challenge Description : 

	This is a old image which I recovered from my old Dad's pc and I can't see anything properly, I guess some bits has been manipulated and My Dad said it has a hidden message for Huge Treasure.
	
#Category:
	Stegnography

#Challenge File:
	Daddy_bits.jpg
	
#Flag : dc1111{1_l0v3_y0u_t00_B1t5}

#Writeup : 

* We get a jpeg file, you may try all string, steghide, binwalk and other stuff too but I guess you might missed jsteg 
* Use jsteg reveal Daddy_bits.jpg and we get link for file download https://mega.nz/file/bfBhzQ5A#i8WGbHF1K39wCxtnfW3yEBTiFPbRaUExY8KgG6JCy94
* Its a png, lets again try binwalk zsteg strings but no results, Since description had a hint about bit manipulation and also but his dad so lets recon about it and we find a tool called appa in github and lets use to decode python3 appa.py -d Chall.png
* We get some random hex digits and lets map out to xxd -r -p Chall.result and find out the file out and its also another png 
* Save that too Flag.png and open it just qr bar image. Lets scan and find it. But it returns **Sorry No Flag here !!**
* lets check String or Exiftool, Comment in image has another link and it has the flag.
