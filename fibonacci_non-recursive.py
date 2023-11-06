import time

n = int(input("Enter number: "))
i = n 
temp = 0 
x = 0
y = 1
start =  time.time()
while i > 0: 
    temp = x
    x = x + y
    y = temp
    i -= 1
    print(y,end=" ")
finish =  time.time()
print("\nTime COmplexity:",finish-start)