num = int(input("Enter the maximum value: "))

a, b = 0, 1
print("Fibonacci Series up to", num, ":")
while a <= num:
    print(a)
    a, b = b, a + b
