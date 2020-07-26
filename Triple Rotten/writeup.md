#Challenge Name : Triple Rotten

#Challenge Description :
    My friend gave this file which prints something with some random character with all same length and some list of number with some number. I guess you can understand this, Can you help me to solve this. and He said to remerber the word triple which may denotes THREE or TROIS or TRE or 3.

#Hint : 
    Not only strings can be rotated even lists can be rotated

#Challenge File : 
    chall.py

#Writeup

    #Solution Script : solve.py

* Just analyse the code you will find function called prime and number which is used just to find least prime number from given number 28101276533935461337993
* Print the least prime and check it would be returing the number 3 (Hint: Title or Description)
* Comment out those number function so that result is printed out immediately, as per program and output it just rotates the flag with length of printable array and list of number and index of each index which is from 0-2 (Which is less than 3)
* The Number in front of each array denotes no of rotation that are made before, so do the opposite rotation to get original position
* Now list has 3 arguments which denotes which index of flag, which lines in above and character from respective array
* Join all character into a single string and you will get a rotten string again 
* As per title/description its encrypted with ROT3 so decrypt with ROT23 and we get the flag "dc1111{Pyth0n_1nd3x1s@w3s0me_Alw@y$}"


### solve.py
"""
import base64

with open("output.txt","rb") as f:
	output=f.readlines()

ar=[]
for i in range(0,99,1):
	ar.append(base64.b64decode(output[i].decode("latin-1").strip()).decode("latin-1"))
	
final=list()
for i in range(101,len(output),1):
	final.append([int(j) for j in output[i].decode('latin-1').strip().split(":")[1].strip().strip('][').split(', ')])

final_flag=""
for i in range(len(final)):
	for _ in range(3-i%3):
		temp=final[i][0]
		for j in range(len(final[i])-1):
			final[i][j]=final[i][j+1]
		final[i][-1]=temp
	final_flag+=ar[final[i][1]][final[i][2]]

for i in final_flag:
	ind = "abcdefghijklmnopqrstuvwxyz".find(i.lower())
	if ind==-1:
		print(i,end="")
	else:
		if i.isupper():
			print("abcdefghijklmnopqrstuvwxyz"[(ind+23)%26].upper(),end="")
		else:
			print("abcdefghijklmnopqrstuvwxyz"[(ind+23)%26],end="")

"""
