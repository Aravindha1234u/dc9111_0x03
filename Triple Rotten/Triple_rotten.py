from string import printable
import random
from flag import flag
import base64 

flag=flag()

def prime(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

def number():
    no="328101276533935461337993"
    b=None
    while len(no)>0:
    	i=int(no)
    	prime(i)
    	if len(str(i))>0:
            b=i
    	no=no[:-1]
    return b

ar=list()
for j in range(1,len(printable)):
    temp=""
    for i in range(len(flag)):
        number()
        temp+=printable[(printable.find(flag[i])+j)%len(printable)]
    ar.append(temp)
    print(str(base64.b64encode(bytes(temp,"utf-8")),"latin-1"))
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
    num=number()
    for _ in range(position.index(i)%num):
        temp=i[0]
        for j in range(len(i)-1):
            i[j]=i[j+1]
        i[-1]=temp
    final.append(i)

for i in range(len(final)):
    print(i%num," : ",final[i])
