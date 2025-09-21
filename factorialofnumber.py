#wap to find factorial of a number n
n = int(input("Enter the value of the number:"))
fact = 1
for i in range(1 , n+1):
    fact *= i
print("Factorial of" , n , "is:", fact)
