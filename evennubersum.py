num = int(input("Enter the no: "))

i = 0
sum = 0

while(i<=num):
    if(i%2 == 0):
        sum += i
    i += 1

print("Sum of",num,"even no is:",sum )