#Fibonacci

n = int(input("Enter the number of Terms: "))

a = 0
b = 1

for _ in range(n):
    print(a)
    c = a + b
    a = b 
    b = c