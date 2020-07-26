from string import printable
import random
from flag import flag

flag=flag()

def prime(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        return True
    else:
        return False

def number():
    no="28101276533935461337993"
    i=int(no)
    b=None
    while i>0:
        prime(i)
        i=int(i/int(no[:-1]))
        if i>1:
            b=i
    return b
num=3
ar=list()
for j in range(1,len(printable)):
    temp=""
    for i in range(len(flag)):
        #number()
        temp+=printable[(printable.find(flag[i])+j)%len(printable)]
    ar.append(temp)
    print(temp)
print("\n")


position=list()
for i in range(len(flag)):
    check=False
    for j in range(len(ar)):
        for k in range(len(ar[j])):
            if(ar[j][k]==flag[i]):
                position.append([i,j,k])
                check=True
                break
        if check==True:
            break
        
final=list()
for i in position:
    #num=number()
    for _ in range(position.index(i)%num):
        temp=i[0]
        for j in range(len(i)-1):
            i[j]=i[j+1]
        i[-1]=temp
    final.append(i)

for i in range(len(final)):
    print(i%num," : ",final[i])

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
