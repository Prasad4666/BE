import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    start = time.time()
    for i in range(n):
        print(fibonacci(i),end=" ")

end = time.time()
print("\nTime Complexity: ",(end-start))