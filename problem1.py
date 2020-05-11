import numpy as np
t=int(input())
a=np.array(list(map(int,input().split())))
b=np.array(list(map(int,input().split())))
count=0
while(0 not in b):
	b-=a
	count+=1
print(count)
