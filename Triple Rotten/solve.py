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

