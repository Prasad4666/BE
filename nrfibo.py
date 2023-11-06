import time

n=int(input("ENter the Number : "))
i=n
temp=0
x=0
y=1

st=time.time()
while i>0:
    temp=x
    x=x+y
    y=temp
    i-=1
    print(y,end=" ")

en=time.time()
print(en-st)