#wap to find factorial of a number n using while loop
n = int(input("Enter the value of the number:"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial of" , n , "is:", fact)
