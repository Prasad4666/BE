import time

def re_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return re_fibo(n-1) + re_fibo(n-2)

n=int(input("Enter: "))
st=time.time()
for i in range(n):
    print(re_fibo(i),end=" ")
end=time.time()
print()
print(end-st)